from flask import Flask, Blueprint
from flask_restful import Api
from resources.resources import ContractResource, ContractListResource, RuleListResource

api_bp = Blueprint('api', __name__)
api = Api(api_bp)


def create_app(config_filename):
    app = Flask(__name__)
    app.config.from_object(config_filename)

    from models.models import db
    db.init_app(app)
    app.register_blueprint(api_bp)

    return app


api.add_resource(ContractResource, '/contracts/<uuid:id>')
api.add_resource(ContractListResource, '/contracts/')
api.add_resource(RuleListResource, '/rules/')
