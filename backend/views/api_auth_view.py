from flask import Blueprint, request, jsonify
from flask_login import login_user, logout_user, current_user, login_required

from backend.services import auth_service
from backend.models.client_error import ValidationError, AuthError
from backend.utils.serializers import serialize_user

api_auth_blueprint = Blueprint("api_auth", __name__, url_prefix="/api/auth")


@api_auth_blueprint.route("/register", methods=["POST"])
def register():
    try:
        data = request.get_json()
        user = auth_service.register(
            first_name=data.get("first_name", ""),
            last_name=data.get("last_name", ""),
            email=data.get("email", ""),
            password=data.get("password", ""),
        )
        login_user(user)
        return jsonify(serialize_user(user)), 201
    except ValidationError as e:
        return jsonify({"error": e.message}), 400
    except AuthError as e:
        return jsonify({"error": e.message}), 401


@api_auth_blueprint.route("/login", methods=["POST"])
def login():
    try:
        data = request.get_json()
        user = auth_service.login(
            email=data.get("email", ""),
            password=data.get("password", ""),
        )
        return jsonify(serialize_user(user)), 200
    except ValidationError as e:
        return jsonify({"error": e.message}), 400
    except AuthError as e:
        return jsonify({"error": e.message}), 401


@api_auth_blueprint.route("/logout", methods=["POST"])
@login_required
def logout():
    auth_service.logout()
    return jsonify({"message": "Logged out"}), 200


@api_auth_blueprint.route("/me", methods=["GET"])
def me():
    if current_user.is_authenticated:
        return jsonify(serialize_user(current_user)), 200
    return jsonify({"error": "Not authenticated"}), 401
