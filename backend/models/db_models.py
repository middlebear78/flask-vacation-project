from flask_login import UserMixin
from backend.extensions import db
from backend.models.role_model import RoleModel


class Role(db.Model):
    __tablename__ = "roles"

    role_id = db.Column(db.Integer, primary_key=True)
    role_name = db.Column(db.String(50), nullable=False)

    users = db.relationship("User", back_populates="role")


class User(UserMixin, db.Model):
    __tablename__ = "users"

    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(256), nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey("roles.role_id"), nullable=False)

    role = db.relationship("Role", back_populates="users")
    likes = db.relationship("Like", back_populates="user", cascade="all, delete-orphan")

    def get_id(self):
        return str(self.user_id)

    @property
    def is_admin(self):
        return self.role_id == RoleModel.Admin.value


class Country(db.Model):
    __tablename__ = "countries"

    country_id = db.Column(db.Integer, primary_key=True)
    country_name = db.Column(db.String(100), nullable=False)

    vacations = db.relationship("Vacation", back_populates="country")


class Vacation(db.Model):
    __tablename__ = "vacations"

    vacation_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    vacation_name = db.Column(db.String(200), nullable=False)
    vacation_description = db.Column(db.Text, nullable=True)
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=False)
    price = db.Column(db.Float, nullable=False)
    vacation_img = db.Column(db.String(255), nullable=True)
    country_id = db.Column(db.Integer, db.ForeignKey("countries.country_id"), nullable=False)
    likes = db.Column(db.Integer, default=0)
    vacation_days = db.Column(db.Integer, default=0)

    country = db.relationship("Country", back_populates="vacations")
    like_records = db.relationship("Like", back_populates="vacation", cascade="all, delete-orphan")

    @property
    def country_name(self):
        return self.country.country_name if self.country else None


class Like(db.Model):
    __tablename__ = "likes"

    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"), primary_key=True)
    vacation_id = db.Column(db.Integer, db.ForeignKey("vacations.vacation_id"), primary_key=True)

    user = db.relationship("User", back_populates="likes")
    vacation = db.relationship("Vacation", back_populates="like_records")
