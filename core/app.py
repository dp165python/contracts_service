from core.api import api_bp, api
from core.resources.resources import ContractResource, ContractListResource, RuleListResource
from flask import Flask
from core.config import runtime_config, db, migrate


app = Flask(__name__)
app.config.from_object(runtime_config())
db.init_app(app)
migrate.init_app(app, db)


app.register_blueprint(api_bp)


api.add_resource(ContractResource, '/contracts/<uuid:id>/')
api.add_resource(ContractListResource, '/contracts/')
api.add_resource(RuleListResource, '/rules/')
