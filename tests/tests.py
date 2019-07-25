import unittest
import json
from core.app import app
from test_data import contract, all_contracts
from core.config import TestConfig


class FlaskTestApi(unittest.TestCase):
    def create_app(self):
        app.config.from_object(TestConfig)
        return app

    def setUp(self):
        self.app = app.test_client()

    def test_get_none_contract(self):
        contract = self.app.get('/contracets/4da90174-8d70-4e5d-bfc8-d075387e41e4')
        self.assertEqual(contract.status_code, 404)

    def test_contract_wrong_address(self):
        contract = self.app.get('/contracets/4da90174-8d70-4e5d-bfc8-d075387e41e3')
        self.assertEqual(contract.status_code, 404)

    def test_contracts_wrong_addresses(self):
        contracts = self.app.get('/contractes/')
        self.assertEqual(contracts.status_code, 404)

    def test_get_all_contracts(self):
        contracts = self.app.get('/contracts/')
        self.assertEqual(contracts.status_code, 200)
        content = json.loads(contracts.get_data(as_text=True))
        self.assertNotEqual(content, all_contracts)


if __name__ == "__main__":
    unittest.main()
