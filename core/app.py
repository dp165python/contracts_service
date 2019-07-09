from flask import Flask


def create_app(config_filename):
    app = Flask(__name__)
    app.config.from_object(config_filename)

    from models.models import db
    db.init_app(app)

    from resources.views import api_bp
    app.register_blueprint(api_bp)

    return app
