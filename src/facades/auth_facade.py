from flask import request, session

from src.logic.auth_logic import AuthLogic
from src.models.client_error import *
from src.models.credentials_model import CredentialModel
from src.models.role_model import RoleModel
from src.utils.cyber import Cyber
from src.models.user_model import UserModel


class AuthFacade:
    def __init__(self):
        self.logic = AuthLogic()

    def register(self):
        first_name = request.form.get("first_name")
        last_name = request.form.get("last_name")
        email = request.form.get("email")
        password = request.form.get("password")

        user = UserModel(None, first_name, last_name, email, password, RoleModel.User.value)
        error = user.validate_insert()
        if error:
            print(f"User validation error: {error}")
            raise ValidationError(error)
        if self.logic.is_email_taken(email):
            print("Email already exists.")
            raise ValidationError("email already exists")
        user.password = Cyber.hash(password)
        return self.logic.add_user(user)

    def login(self):
        email = request.form.get("email")
        password = request.form.get("password")


        user = self.logic.get_user_by_email(email)

        if not user or Cyber.hash(password) != user["password"]:
            raise AuthError("Incorrect Email or Password", user)

        del user["password"]  # Remove password before storing in session
        session["current_user"] = user

    def block_anonymous(self):
        user = session.get("current_user")
        if not user: raise AuthError("You are not logged in", user)

    def block_non_admin(self):
        user = session.get("current_user")
        if not user: raise AuthError("You are not logged in", user)
        if user["role_id"] != RoleModel.Admin.value: raise AuthError("You are not allowed.", user)

    def close(self):
        self.logic.close()

    def logout(self):
        session.clear()
