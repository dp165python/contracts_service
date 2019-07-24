import unittest
from manage import app
from core.config import TestConfig


class FlaskTestApi(unittest.TestCase):
    def create_app(self):
        core.config.from_object(TestConfig)
        return app

    def setUp(self):
        self.app = app.test_client()

    def test_get_none_contract(self):
        contract = self.app.get('/contracts/4da90174-8d70-4e5d-bfc8-d075387e41e4')
        self.assertEqual(contract.status_code, 404)

    def test_contract_wrong_address(self):
        contract = self.app.get('/contracets/4da90174-8d70-4e5d-bfc8-d075387e41e3')
        self.assertEqual(contract.status_code, 404)

    def test_contracts_wrong_addresses(self):
        contracts = self.app.get('/contractes/')
        self.assertEqual(contracts.status_code, 404)


if __name__ == "__main__":
    unittest.main()
