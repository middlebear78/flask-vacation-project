from backend.models.db_models import Country


def get_all_countries():
    return Country.query.order_by(Country.country_name.asc()).all()
