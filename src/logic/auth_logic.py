from src.utils.dal import DAL


class AuthLogic:

    def __init__(self) -> None:
        self.dal = DAL()

    def add_user(self, user):
        query = "INSERT INTO users(first_name, last_name, email, password, role_id) VALUES(%s, %s, %s,%s, %s)"
        return self.dal.insert(query, (user.first_name, user.last_name, user.email, user.password, user.role_id))

    def is_email_taken(self, email):
        query = "SELECT COUNT(*) AS count FROM users WHERE email = %s"
        result = self.dal.get_scalar(query, (email,))
        print(f"Email check result: {result}")
        return result["count"] > 0

    def get_user(self, credentials):
        query = "SELECT * FROM users WHERE email = %s and password = %s"
        user = self.dal.get_scalar(query, (credentials.email, credentials.password))
        return user

    def get_user_by_email(self, email):
        query = "SELECT * FROM users WHERE email = %s"
        user = self.dal.get_scalar(query, (email,))
        return user

    def close(self):
        self.dal.close();
