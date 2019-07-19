from flask import request
from flask_restful import Resource

from core import status
from core.controllers.controllers import ContractListController, ContractController, RuleListController
from core.models.models import db, Rule, Contract
from core.schemas.schemas import rule_schema, contract_schema


class ContractResource(Resource):
    def get(self, id):
        one_contract = ContractController().get_one_contract(id)
        return contract_schema.dump(one_contract).data


class ContractListResource(Resource):
    def get(self):
        all_contracts = ContractListController().get_all_contracts()
        return contract_schema.dump(all_contracts, many=True).data

    def post(self):
        request_dict = request.get_json() or {}
        post_contract = ContractListController.post_contract(id, request_dict)
        return contract_schema.dump(post_contract).data, status.HTTP_201_CREATED


class RuleListResource(Resource):
    def post(self, id):
        request_dict = request.get_json() or {}
        post_rule = RuleListController.post_rule(self, request_dict, id)
        return rule_schema.dump(post_rule).data, status.HTTP_201_CREATED

    # def post(self):
    #     request_dict = request.get_json()
    #     contract_name = request_dict['contract']['name']
    #     contract = Contract.query.filter_by(name=contract_name).first()
    #     if contract is None:
    #         # create a new contract
    #         contract = Contract(name=contract_name,
    #                             information=request_dict['information'])
    #         db.session.add(contract)
    #     # create a new rule
    #     rule = Rule(
    #         rule_name=request_dict['rule_name'],
    #         f_operand=request_dict['f_operand'],
    #         s_operand=request_dict['s_operand'],
    #         operator=request_dict['operator'],
    #         coefficient=request_dict['coefficient'],
    #         contract=contract)
    #     rule.add(rule)
    #     query = Rule.query.get(rule.id)
    #     return rule_schema.dump(query).data, status.HTTP_201_CREATED