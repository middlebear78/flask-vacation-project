from flask import Blueprint, render_template, send_file, url_for, redirect, request, session, jsonify, flash

from src.facades.auth_facade import AuthFacade
from src.facades.countries_facade import CountriesFacade
from src.facades.like_facade import LikeFacade
from src.facades.vacation_facade import VacationFacade
from src.models.client_error import ValidationError
from src.models.role_model import *
from src.utils.image_handler import ImageHandler

vacations_blueprint = Blueprint("vacations_view", __name__)
auth_facade = AuthFacade()
facade = VacationFacade()
like_facade = LikeFacade()


@vacations_blueprint.route("/vacations")
def list():
    current_user = session.get('current_user')

    if not current_user:
        flash("You need to log in to view this page", "danger")
        return redirect(url_for("auth_view.login"))

    all_vacations = facade.get_all_vacations()
    user_likes = []

    if current_user:
        user_likes_data = like_facade.get_all_likes_for_user(user_id=current_user.get("user_id"))
        user_likes = [like['vacation_id'] for like in user_likes_data]


    return render_template("vacations.html", vacations=all_vacations, active="vacations",
                           current_user=current_user, admin=RoleModel.Admin.value,
                           user=RoleModel.User.value, user_likes=user_likes)





@vacations_blueprint.route("/vacations/images/<string:image_name>")
def get_image(image_name):
    image_path = ImageHandler.get_image_path(image_name)
    return send_file(image_path)


@vacations_blueprint.route("/vacations/new", methods=["GET", "POST"])
def add_vacation():
    if request.method == "GET":
        country_facade = CountriesFacade()
        countries = country_facade.get_all_countries()
        return render_template("add_vacation.html", active="new", countries=countries)

    if request.method == "POST":
        try:
            facade.add_vacation()
            flash("Vacation added successfully!", "success")
            return redirect(url_for("vacations_view.list"))
        except ValidationError as e:

            flash(str(e), "danger")

            country_facade = CountriesFacade()
            countries = country_facade.get_all_countries()
            return render_template("add_vacation.html", active="new", countries=countries)


@vacations_blueprint.route("/vacations/edit/<int:vacation_id>", methods=["GET", "POST"])
def edit_vacation(vacation_id):
    auth_facade.block_non_admin()
    country_facade = CountriesFacade()

    countries = country_facade.get_all_countries()

    if request.method == "GET":
        one_vacation = facade.get_one_vacation(vacation_id)
        return render_template("edit_vacation.html", vacation=one_vacation, countries=countries)

    try:
        facade.update_vacation()
        flash("Vacation updated successfully!", "success")

        return redirect(url_for("vacations_view.list"))
    except ValidationError as e:
        flash(str(e), "danger")

        one_vacation = facade.get_one_vacation(vacation_id)
        return render_template("edit_vacation.html", vacation=one_vacation, countries=countries)


@vacations_blueprint.route("/vacations/delete/<int:id>")
def delete_vacation(id):
    facade.delete_vacation(id)
    flash("Vacation deleted successfully!", "success")

    return redirect(url_for("vacations_view.list"))


@vacations_blueprint.route('/like_vacation/<int:user_id>/<int:vacation_id>/', methods=['POST'])
def like_vacation(user_id, vacation_id):
    result = like_facade.add_like(user_id=user_id, vacation_id=vacation_id)
    return jsonify(result)


@vacations_blueprint.route('/unlike_vacation/<int:user_id>/<int:vacation_id>/', methods=['DELETE'])
def unlike_vacation(user_id, vacation_id):
    result = like_facade.del_like(user_id=user_id, vacation_id=vacation_id)
    return jsonify(result)
