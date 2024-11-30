from email_validator import validate_email

from src.models.role_model import RoleModel


class UserModel:

    def __init__(self, user_id, first_name, last_name, email, password, role_id):
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.role_id = role_id

    def validate_insert(self):
        if not self.first_name: return "missing first_name"
        if not self.last_name: return "missing last_name"
        if not self.email: return "missing email"
        if not self.password: return "missing password"
        if not self.role_id: return "missing role id"
        if len(self.first_name) < 2 or len(self.first_name) > 20: return "first name must be 1-20 characters long"
        if len(self.last_name) < 2 or len(self.last_name) > 20: return "last name must be 1-20 characters long"
        if len(self.password) < 4 or len(self.password) > 20: return "password must be 4-20 characters long"
        if not validate_email(self.email): return "email not valid"
        if self.role_id != RoleModel.Admin.value and self.role_id != RoleModel.User.value: "not valid role"
        return None
