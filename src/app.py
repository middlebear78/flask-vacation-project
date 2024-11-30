from flask import Flask, render_template
from flask_login import current_user

from src.models.role_model import RoleModel
from src.utils.app_config import AppConfig
from src.views.about_view import about_blueprint
from src.views.auth_view import auth_blueprint
from src.views.home_view import home_blueprint
from src.views.vacations_view import vacations_blueprint

app = Flask(__name__)

app.secret_key = AppConfig.session_secret_key
app.register_blueprint(home_blueprint)
app.register_blueprint(about_blueprint)
app.register_blueprint(vacations_blueprint)
app.register_blueprint(auth_blueprint)


@app.context_processor
def inject_user():
    return dict(current_user=current_user, admin=RoleModel.Admin.value)


@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html")


@app.errorhandler(Exception)
def catch_all(error):
    print(error)
    return render_template('500.html', error=error)


if __name__ == '__main__':
    app.run(debug=True)
