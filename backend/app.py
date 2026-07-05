import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from flask import Flask, jsonify, send_from_directory
from flask_login import current_user

from backend.extensions import db, migrate, login_manager, csrf
from backend.models.role_model import RoleModel
from backend.utils.app_config import AppConfig

FRONTEND_DIR = os.path.join(os.path.dirname(__file__), '..', 'frontend')
UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), 'uploads', 'images')


def create_app():
    app = Flask(
        __name__,
        static_folder=os.path.join(FRONTEND_DIR, 'dist', 'assets'),
        static_url_path='/assets',
    )

    app.config["SECRET_KEY"] = AppConfig.session_secret_key
    app.config["SQLALCHEMY_DATABASE_URI"] = AppConfig.get_sqlalchemy_uri()
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
    app.config["SESSION_COOKIE_SAMESITE"] = "Lax"

    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    csrf.init_app(app)

    from backend.models.db_models import User

    @login_manager.user_loader
    def load_user(user_id):
        return db.session.get(User, int(user_id))

    @login_manager.unauthorized_handler
    def unauthorized():
        return jsonify({"error": "Authentication required"}), 401

    # API blueprints
    from backend.views.api_auth_view import api_auth_blueprint
    from backend.views.api_vacations_view import api_vacations_blueprint
    from backend.views.api_countries_view import api_countries_blueprint

    app.register_blueprint(api_auth_blueprint)
    app.register_blueprint(api_vacations_blueprint)
    app.register_blueprint(api_countries_blueprint)

    # Exempt API blueprints from CSRF (session cookies with SameSite=Lax are sufficient)
    csrf.exempt(api_auth_blueprint)
    csrf.exempt(api_vacations_blueprint)
    csrf.exempt(api_countries_blueprint)

    # Serve React build in production (catch-all)
    dist_dir = os.path.join(FRONTEND_DIR, 'dist')

    @app.route('/', defaults={'path': ''})
    @app.route('/<path:path>')
    def serve_react(path):
        # Don't intercept /api/ routes
        if path.startswith('api/'):
            return jsonify({"error": "Not found"}), 404

        file_path = os.path.join(dist_dir, path)
        if path and os.path.isfile(file_path):
            return send_from_directory(dist_dir, path)
        return send_from_directory(dist_dir, 'index.html')

    return app


app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
