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
        contract = self.app.get('/contracts/none_contract')
        self.assertEqual(contract.status_code, 404)

    def test_contracts_wrong_address(self):
        contracts = self.app.get('/contractes/')
        self.assertEqual(contracts.status_code, 404)


if __name__ == "__main__":
    unittest.main()
