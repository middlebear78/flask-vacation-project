from backend.models.role_model import RoleModel


def serialize_user(user):
    return {
        "user_id": user.user_id,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "email": user.email,
        "role_id": user.role_id,
        "is_admin": user.role_id == RoleModel.Admin.value,
    }


def serialize_vacation(vacation, is_liked=False):
    return {
        "vacation_id": vacation.vacation_id,
        "vacation_name": vacation.vacation_name,
        "vacation_description": vacation.vacation_description,
        "start_date": vacation.start_date.isoformat() if vacation.start_date else None,
        "end_date": vacation.end_date.isoformat() if vacation.end_date else None,
        "price": vacation.price,
        "vacation_img": vacation.vacation_img,
        "country_id": vacation.country_id,
        "country_name": vacation.country_name,
        "likes": vacation.likes or 0,
        "vacation_days": vacation.vacation_days or 0,
        "is_liked": is_liked,
    }


def serialize_country(country):
    return {
        "country_id": country.country_id,
        "country_name": country.country_name,
    }
