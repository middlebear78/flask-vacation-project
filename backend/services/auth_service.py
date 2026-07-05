from flask_login import login_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash

from backend.extensions import db
from backend.models.db_models import User
from backend.models.role_model import RoleModel
from backend.models.client_error import ValidationError, AuthError
from backend.utils.cyber import Cyber


def register(first_name, last_name, email, password):
    if not first_name:
        raise ValidationError("missing first_name")
    if not last_name:
        raise ValidationError("missing last_name")
    if not email:
        raise ValidationError("missing email")
    if not password:
        raise ValidationError("missing password")
    if len(first_name) < 2 or len(first_name) > 20:
        raise ValidationError("first name must be 2-20 characters long")
    if len(last_name) < 2 or len(last_name) > 20:
        raise ValidationError("last name must be 2-20 characters long")
    if len(password) < 4 or len(password) > 20:
        raise ValidationError("password must be 4-20 characters long")

    existing = User.query.filter_by(email=email).first()
    if existing:
        raise ValidationError("email already exists")

    user = User(
        first_name=first_name,
        last_name=last_name,
        email=email,
        password=generate_password_hash(password),
        role_id=RoleModel.User.value,
    )
    db.session.add(user)
    db.session.commit()
    return user


def login(email, password):
    if not email:
        raise ValidationError("Please provide an email account")
    if not password:
        raise ValidationError("Please provide a password")

    user = User.query.filter_by(email=email).first()
    if not user:
        raise AuthError("Incorrect Email or Password")

    # Try modern werkzeug hash first
    if check_password_hash(user.password, password):
        login_user(user)
        return user

    # Fallback: try legacy SHA-512 hash and migrate if it matches
    legacy_hash = Cyber.hash(password)
    if user.password == legacy_hash:
        user.password = generate_password_hash(password)
        db.session.commit()
        login_user(user)
        return user

    raise AuthError("Incorrect Email or Password")


def logout():
    logout_user()
