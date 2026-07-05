from flask import Blueprint, request, jsonify, send_from_directory, current_app
from flask_login import current_user, login_required

from backend.services import vacation_service, like_service
from backend.models.client_error import ValidationError
from backend.utils.serializers import serialize_vacation

api_vacations_blueprint = Blueprint("api_vacations", __name__, url_prefix="/api/vacations")


@api_vacations_blueprint.route("/", methods=["GET"])
@login_required
def get_all():
    vacations = vacation_service.get_all_vacations()
    liked_ids = like_service.get_user_liked_vacation_ids(current_user.user_id)
    result = [
        serialize_vacation(v, is_liked=(v.vacation_id in liked_ids))
        for v in vacations
    ]
    return jsonify(result), 200


@api_vacations_blueprint.route("/<int:vacation_id>", methods=["GET"])
@login_required
def get_one(vacation_id):
    try:
        vacation = vacation_service.get_one_vacation(vacation_id)
        liked_ids = like_service.get_user_liked_vacation_ids(current_user.user_id)
        return jsonify(serialize_vacation(vacation, is_liked=(vacation.vacation_id in liked_ids))), 200
    except ValidationError as e:
        return jsonify({"error": e.message}), 404


@api_vacations_blueprint.route("/", methods=["POST"])
@login_required
def create():
    if not current_user.is_admin:
        return jsonify({"error": "Admin access required"}), 403
    try:
        vacation = vacation_service.add_vacation(
            vacation_name=request.form.get("vacation_name", ""),
            vacation_description=request.form.get("vacation_description", ""),
            start_date=request.form.get("start_date", ""),
            end_date=request.form.get("end_date", ""),
            price=request.form.get("price", ""),
            image=request.files.get("vacation_image"),
            country_name=request.form.get("country", ""),
        )
        return jsonify(serialize_vacation(vacation)), 201
    except ValidationError as e:
        return jsonify({"error": e.message}), 400


@api_vacations_blueprint.route("/<int:vacation_id>", methods=["PUT"])
@login_required
def update(vacation_id):
    if not current_user.is_admin:
        return jsonify({"error": "Admin access required"}), 403
    try:
        vacation = vacation_service.update_vacation(
            vacation_id=vacation_id,
            vacation_name=request.form.get("vacation_name", ""),
            vacation_description=request.form.get("vacation_description", ""),
            start_date=request.form.get("start_date", ""),
            end_date=request.form.get("end_date", ""),
            price=request.form.get("price", ""),
            image=request.files.get("vacation_image"),
            country_name=request.form.get("country", ""),
        )
        return jsonify(serialize_vacation(vacation)), 200
    except ValidationError as e:
        return jsonify({"error": e.message}), 400


@api_vacations_blueprint.route("/<int:vacation_id>", methods=["DELETE"])
@login_required
def delete(vacation_id):
    if not current_user.is_admin:
        return jsonify({"error": "Admin access required"}), 403
    try:
        vacation_service.delete_vacation(vacation_id)
        return jsonify({"message": "Vacation deleted"}), 200
    except ValidationError as e:
        return jsonify({"error": e.message}), 400


@api_vacations_blueprint.route("/<int:vacation_id>/like", methods=["POST"])
@login_required
def like(vacation_id):
    count = like_service.add_like(current_user.user_id, vacation_id)
    return jsonify({"likes": count}), 200


@api_vacations_blueprint.route("/<int:vacation_id>/like", methods=["DELETE"])
@login_required
def unlike(vacation_id):
    count = like_service.remove_like(current_user.user_id, vacation_id)
    return jsonify({"likes": count}), 200


@api_vacations_blueprint.route("/images/<path:name>", methods=["GET"])
def get_image(name):
    upload_folder = current_app.config.get("UPLOAD_FOLDER")
    return send_from_directory(upload_folder, name)
