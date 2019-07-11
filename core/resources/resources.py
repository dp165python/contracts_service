from flask import Blueprint, request, jsonify, make_response
from flask_restful import Api, Resource
from models.models import db, Rule, Contract
from schemas.schemas import RuleSchema, ContractSchema
from sqlalchemy.exc import SQLAlchemyError
import status
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4


api_bp = Blueprint('api', __name__)
api = Api(api_bp)

contract_schema = ContractSchema()
rule_schema = RuleSchema()


class ContractResource(Resource):
    def get(self, id):
        contract = Contract.query.get_or_404(id)
        result = contract_schema.dump(contract).data
        return result


class ContractListResource(Resource):
    def get(self):
        contracts = Contract.query.all()
        results = contract_schema.dump(contracts, many=True).data
        return results

    def post(self):
        request_dict = request.get_json()
        if not request_dict:
            resp = {'message': 'No input data provided'}
            return resp, status.HTTP_400_BAD_REQUEST
        errors = contract_schema.validate(request_dict)
        if errors:
            return errors, status.HTTP_400_BAD_REQUEST
        try:
            contract = Contract(
                name=request_dict['name'],
                information=request_dict['information'])
            contract.add(contract)
            query = Contract.query.get(contract.id)
            result = contract_schema.dump(query).data
            return result, status.HTTP_201_CREATED
        except SQLAlchemyError as e:
            db.session.rollback()
            resp = jsonify({"error": str(e)})
            return resp, status.HTTP_400_BAD_REQUEST


class RuleListResource(Resource):
    def get(self):
        rules = Rule.query.all()
        result = rule_schema.dump(rules, many=True).data
        return result

    def post(self):
        request_dict = request.get_json()
        if not request_dict:
            response = {'message': 'No input data provided'}
            return response, status.HTTP_400_BAD_REQUEST
        errors = rule_schema.validate(request_dict)
        if errors:
            return errors, status.HTTP_400_BAD_REQUEST
        try:
            contract_name = request_dict['contract']['name']
            contract = Contract.query.filter_by(name=contract_name).first()
            if contract is None:
                # create a new contract
                contract = Contract(name=contract_name,
                                    information=request_dict['information'])
                db.session.add(contract)
            # create a new rule
            rule = Rule(
                rule_name=request_dict['rule_name'],
                f_operand=request_dict['f_operand'],
                s_operand=request_dict['s_operand'],
                operator=request_dict['operator'],
                coefficient=request_dict['coefficient'],
                contract=contract)
            rule.add(rule)
            query = Rule.query.get(rule.id)
            result = rule_schema.dump(query).data
            return result, status.HTTP_201_CREATED
        except SQLAlchemyError as e:
            db.session.rollback()
            resp = jsonify({"error": str(e)})
            return resp, status.HTTP_400_BAD_REQUEST


api.add_resource(ContractListResource, '/contracts/')
api.add_resource(ContractResource, '/contracts/<uuid:id>')
api.add_resource(RuleListResource, '/rules/')
