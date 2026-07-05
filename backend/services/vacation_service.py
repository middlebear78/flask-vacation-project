from datetime import datetime

from backend.extensions import db
from backend.models.db_models import Vacation, Country
from backend.models.client_error import ValidationError
from backend.utils.image_handler import ImageHandler


def get_all_vacations():
    return (
        Vacation.query
        .join(Country)
        .order_by(Vacation.start_date.asc())
        .all()
    )


def get_one_vacation(vacation_id):
    vacation = db.session.get(Vacation, vacation_id)
    if not vacation:
        raise ValidationError(f"Vacation with id {vacation_id} not found.")
    return vacation


def add_vacation(vacation_name, vacation_description, start_date, end_date, price, image, country_name):
    _validate_vacation_fields(vacation_name, vacation_description, start_date, end_date, price, country_name)
    _validate_image_required(image)

    start_dt = datetime.strptime(start_date, "%Y-%m-%d").date()
    end_dt = datetime.strptime(end_date, "%Y-%m-%d").date()

    country = Country.query.filter_by(country_name=country_name).first()
    if not country:
        raise ValidationError(f"Country '{country_name}' not found.")

    image_name = ImageHandler.save_image(image)
    vacation_days = (end_dt - start_dt).days + 1

    vacation = Vacation(
        vacation_name=vacation_name,
        vacation_description=vacation_description,
        start_date=start_dt,
        end_date=end_dt,
        price=float(price),
        vacation_img=image_name,
        country_id=country.country_id,
        likes=0,
        vacation_days=vacation_days,
    )
    db.session.add(vacation)
    db.session.commit()
    return vacation


def update_vacation(vacation_id, vacation_name, vacation_description, start_date, end_date, price, image, country_name):
    _validate_vacation_fields(vacation_name, vacation_description, start_date, end_date, price, country_name)

    vacation = db.session.get(Vacation, int(vacation_id))
    if not vacation:
        raise ValidationError("Vacation not found.")

    start_dt = datetime.strptime(start_date, "%Y-%m-%d").date()
    end_dt = datetime.strptime(end_date, "%Y-%m-%d").date()

    country = Country.query.filter_by(country_name=country_name).first()
    if not country:
        raise ValidationError(f"Country '{country_name}' not found.")

    image_name = ImageHandler.update_image(vacation.vacation_img, image)

    vacation.vacation_name = vacation_name
    vacation.vacation_description = vacation_description
    vacation.start_date = start_dt
    vacation.end_date = end_dt
    vacation.price = float(price)
    vacation.vacation_img = image_name
    vacation.country_id = country.country_id
    vacation.vacation_days = (end_dt - start_dt).days + 1

    db.session.commit()
    return vacation


def delete_vacation(vacation_id):
    vacation = db.session.get(Vacation, vacation_id)
    if not vacation:
        raise ValidationError("Vacation does not exist in the Database.")
    ImageHandler.delete_image(vacation.vacation_img)
    db.session.delete(vacation)
    db.session.commit()


def _validate_vacation_fields(vacation_name, vacation_description, start_date, end_date, price, country_name):
    missing = []
    if not vacation_name:
        missing.append("vacation_name")
    if not vacation_description:
        missing.append("vacation_description")
    if not start_date:
        missing.append("start_date")
    if not end_date:
        missing.append("end_date")
    if not price and price != 0:
        missing.append("price")
    if not country_name:
        missing.append("country_name")
    if missing:
        raise ValidationError(f"The following fields are required: {', '.join(missing)}")

    try:
        price_val = float(price)
    except (ValueError, TypeError):
        raise ValidationError("Price must be a valid number.")
    if not (0 <= price_val <= 10000):
        raise ValidationError("Price must be between 0 and 10,000.")

    start_dt = datetime.strptime(start_date, "%Y-%m-%d").date()
    end_dt = datetime.strptime(end_date, "%Y-%m-%d").date()
    if start_dt > end_dt:
        raise ValidationError("Start date cannot exceed end date.")


def _validate_image_required(image):
    if not image or not image.filename:
        raise ValidationError("Vacation image is required.")
