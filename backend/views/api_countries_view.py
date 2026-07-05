from flask import Blueprint, jsonify
from flask_login import login_required

from backend.services import country_service
from backend.utils.serializers import serialize_country

api_countries_blueprint = Blueprint("api_countries", __name__, url_prefix="/api/countries")


@api_countries_blueprint.route("/", methods=["GET"])
@login_required
def get_all():
    countries = country_service.get_all_countries()
    return jsonify([serialize_country(c) for c in countries]), 200
