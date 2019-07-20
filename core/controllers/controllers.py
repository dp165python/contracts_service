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
