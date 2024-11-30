from flask import Blueprint, render_template, url_for, redirect, request, flash

from src.facades.auth_facade import AuthFacade
from src.models.client_error import *

auth_blueprint = Blueprint("auth_view", __name__)

facade = AuthFacade()


@auth_blueprint.route("/register", methods=["GET", "POST"])
def register():
    try:
        if request.method == "GET": return render_template("register.html", active="register")
        facade.register()
        facade.login()
        flash("Registration successful, you are now logged in!", "success")

        return redirect(url_for("vacations_view.list"))
    except ValidationError as err:
        flash(err.message, "danger")
        return render_template("register.html", error=err.message, user=err.model)


@auth_blueprint.route("/login", methods=["GET", "POST"])
def login():
    try:
        if request.method == "GET":
            return render_template("login.html", credentials={}, active="login")
        facade.login()
        flash("You are currently logged in!", "success")
        return redirect(url_for("vacations_view.list"))
    except (ValidationError, AuthError) as err:
        return render_template("login.html", error=err.message, credentials=err.model, active="login")


@auth_blueprint.route("/logout")
def logout():
    facade.logout()
    flash("You are currently logged out!", "success")

    return redirect(url_for("home_view.home"))
