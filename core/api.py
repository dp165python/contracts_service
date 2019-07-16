from flask import Blueprint, request, jsonify, make_response
from flask_restful import Api, Resource
from models.models import db, Rule, Contract
from schemas.schemas import RuleSchema, ContractSchema
from sqlalchemy.exc import SQLAlchemyError
import status
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4
from resources.resources import ContractResource, ContractListResource, RuleListResource


api_bp = Blueprint('api', __name__)
api = Api(api_bp)

api.add_resource(ContractResource, '/contracts/<uuid:id>')
api.add_resource(ContractListResource, '/contracts/')
api.add_resource(RuleListResource, '/rules/')
