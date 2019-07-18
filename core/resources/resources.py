from flask import Blueprint, request, jsonify, make_response
from flask_restful import Api, Resource
from core.models.models import db, Rule, Contract
from core.schemas.schemas import RuleSchema, ContractSchema
from sqlalchemy.exc import SQLAlchemyError
from core import status
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4


contract_schema = ContractSchema()
rule_schema = RuleSchema()


class ContractResource(Resource):
    def get(self, id):
        return contract_schema.dump(Contract.query.get_or_404(id)).data


class ContractListResource(Resource):
    def get(self):
        return contract_schema.dump(Contract.query.all(), many=True).data

    def post(self):
        request_dict = request.get_json() or {}
        contract = Contract(
            name=request_dict['name'],
            information=request_dict['information'])
        db.session.add(contract)
        db.session.commit()
        return contract_schema.dump(Contract.query.get(contract.id)).data, status.HTTP_201_CREATED


class RuleListResource(Resource):
    def get(self):
        return rule_schema.dump(Rule.query.all(), many=True).data

    def post(self, id):
        contract = Contract.query.get_or_404(id)
        request_dict = request.get_json() or {}
        rule = Rule(
            rule_name=request_dict['rule_name'],
            f_operand=request_dict['f_operand'],
            s_operand=request_dict['s_operand'],
            operator=request_dict['operator'],
            coefficient=request_dict['coefficient'],
            contract=contract)
        db.session.add(rule)
        db.session.commit()
        return rule_schema.dump(Rule.query.get(rule.id)).data, status.HTTP_201_CREATED
