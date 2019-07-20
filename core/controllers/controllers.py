from core.app import db
from core.models.models import Contract, Rule


class ContractController():
    def get_one_contract(self, id):
        one_contract = Contract.query.get_or_404(id)
        return one_contract


class ContractListController():
    def get_all_contracts(self):
        all_contracts = Contract.query.all()
        return all_contracts

    def post_contract(self, request_dict):
        name = request_dict['name']
        information = request_dict['information']
        contract = Contract(name=name, information=information)
        db.session.add(contract)
        db.session.commit()
        return contract


class RuleListController():
    def post_rule(self, request_dict, id):
        contract_id = Contract.query.get_or_404(id)
        rule_name = request_dict['rule_name']
        f_operand = request_dict['f_operand']
        s_operand = request_dict['s_operand']
        operator = request_dict['operator']
        coefficient = request_dict['coefficient']
        rule = Rule(rule_name=rule_name, f_operand=f_operand, s_operand=s_operand, operator=operator,
                    coefficient=coefficient, contract=contract_id)
        db.session.add(rule)
        db.session.commit()
        return rule
