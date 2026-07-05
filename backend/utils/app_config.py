from dotenv import load_dotenv
from os import environ

load_dotenv()


class AppConfig:
    is_development = environ.get("ENVIRONMENT") == "development"
    is_production = environ.get("ENVIRONMENT") == "production"
    mysql_host = environ.get("MYSQL_HOST")
    mysql_user = environ.get("MYSQL_USER")
    mysql_password = environ.get("MYSQL_PASSWORD")
    mysql_database = environ.get("MYSQL_DATABASE")
    session_secret_key = environ.get("SESSION_SECRET_KEY")
    password_salt = environ.get("PASSWORD_SALT")

    @staticmethod
    def get_sqlalchemy_uri():
        user = environ.get("MYSQL_USER")
        password = environ.get("MYSQL_PASSWORD")
        host = environ.get("MYSQL_HOST")
        database = environ.get("MYSQL_DATABASE")
        return f"mysql+pymysql://{user}:{password}@{host}/{database}"
