from src.models.user_model import UserModel
from src.utils.dal import *


class UserLogic:
    def __init__(self):
        self.dal = DAL()

    def add_user(self, first_name, last_name, email, password, role_id="user"):
        params = (first_name, last_name, email, password, role_id)
        query = (
            "INSERT INTO users (first_name, last_name, email, password, role_id) "
            " VALUES (%s,%s,%s,%s,(SELECT role_id FROM roles WHERE role_name=%s))"
        )
        result = self.dal.insert(query, params)
        if result:
            print("User added successfully.")
            return True
        else:
            raise ValueError("Failed to add user.")

    def get_user(self, email, password):
        params = (email, password)
        query = """SELECT users.user_id, users.first_name, users.last_name, users.email, users.password, roles.role_name
                    FROM users
                    INNER JOIN roles ON users.role_id = roles.role_id
                    WHERE users.email = %s AND users.password = %s
                    """
        result = self.dal.get_table(query, params)
        if result:
            result = UserModel.dict_to_user(result[0])
            print("Retrieving User from DataBase:")
            print(result)
            return result
        else:
            raise ValueError("Cannot Retrieve user.")

    def check_email_exists(self, email):
        query = "SELECT * FROM users WHERE email = %s"
        params = (email,)
        result = self.dal.get_table(query, params)
        return bool(result)

    def validate_password(self, password):
        query = "SELECT * FROM users WHERE password = %s"
        params = (password,)
        result = self.dal.get_table(query, params)
        return bool(result)

    def check_user_exists(self, user_id):
        query = "SELECT * FROM users WHERE user_id = %s"
        params = (user_id,)
        result = self.dal.get_table(query, params)
        return bool(result)
