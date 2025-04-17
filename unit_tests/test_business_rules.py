import unittest
import json
from app import create_app
from unit_tests.base_test_setup import BaseTest


class BusinessRulesApiTestCase(BaseTest):

    def test_successful_processor_determination(self):
        payload = {
            "booking_datetime": "2025-04-05 10:55:00",
            "departure_scheduled_datetime": "2099-04-19 15:25:00",
            "card_type": "Mastercard",
            "bin_number": "520275",
            "transaction_amount": 5956,
            "currency_code": "CAD",
            "source": "FLAIROCI",
            "applied_3ds": True,
            "country": "Canada",
            "departurecity": "YYZ",
            "destinationcity": "YEG"
        }
        response = self.client.post('/rules', json=payload)
        self.assertEqual(response.status_code, 200)
        #self.assertEqual(response.data, "")
        self.assertEqual(response.get_json()["data"],"Elavon")