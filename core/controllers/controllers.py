import uuid
from flask_restful import abort
from models import Contract, Rules
from resources.resources import ContractResource, ContractListResource, RuleListResource
from flask import g


class ContractController:
    def __init__(self, data, errors):
        self._data = data
        self._errors = errors

    def contract_create(self):
        contract = Contract(
            name=self._data['name'],
            information=self._data['information'])
        #contract.add(contract)
        #g.db.session(contract)

        return contract.id
