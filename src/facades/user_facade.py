import re
from src.logic.user_logic import UserLogic
from src.logic.vacation_logic import VacationLogic
from src.utils.dal import DAL


class UserFacade:
    PARAM_COUNT = 4

    def __init__(self):
        self.params = {"first_name": "", "last_name": "", "email": "", "password": ""}
        self.dal = DAL()
        self.user_logic = UserLogic()
        self.vacation_logic = VacationLogic()

    def validate_params(self):
        self._check_param_count()
        self._check_param_values()
        self._check_password_length()
        self._check_email_format()
        self._check_unique_email()
        return all(self.params.values())

    def validate_login(self):
        self._check_login_param_values()
        self._check_password_length()
        return self.user_logic.check_email_exists(
            self.params["email"]
        ) and self.user_logic.validate_password(self.params["password"])

    def _check_param_count(self):
        if len(self.params) != self.PARAM_COUNT:
            raise ValueError("All parameters must be filled in to add a user.\n")

    def _check_param_values(self):
        if not all(self.params.values()):
            raise ValueError("You must fill in all fields to register.\n")

    def _check_password_length(self):
        if len(self.params["password"]) < 4:
            raise ValueError("Password must be at least 4 characters.\n")

    def _check_email_format(self):
        expression = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        if not re.match(expression, self.params["email"]):
            raise ValueError("Please provide a valid email address.\n")

    def _check_unique_email(self):
        if self.user_logic.check_email_exists(self.params["email"]):
            raise ValueError(
                "User email already exists. Please choose another email.\n"
            )

    def _check_login_param_values(self):

        if "email" not in self.params or "password" not in self.params:
            raise ValueError("Both email and password are required to log in.\n")

        if not self.params["email"] or not self.params["password"]:
            raise ValueError("You must fill in Both email and password to log in.\n")

    def add_user(self):
        if self.validate_params():
            self.user_logic.add_user(
                self.params["first_name"],
                self.params["last_name"],
                self.params["email"],
                self.params["password"],
            )
            self._clear_params()

    def log_in(self):
        if not self.validate_login():
            raise ValueError("User email or password invalid.\n")
        result = self.user_logic.get_user(self.params["email"], self.params["password"])
        print("Successfully logged in.")
        self._clear_params()
        return result

    def _clear_params(self):
        self.params = {"first_name": "", "last_name": "", "email": "", "password": ""}

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.dal.close()



