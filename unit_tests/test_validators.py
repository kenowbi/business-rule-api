from app.services.business_rule_service import BusinessRuleService
from app.validators.creditcard_validator import validate_credit_card_type
from app.validators.currency_code_validator import validate_currency_code
from app.validators.departure_date_validator import validate_departure_date
from app.validators.source_validator import validate_source
from unit_tests.base_test_setup import BaseTest
from datetime import datetime, timedelta


class ValidatorRulesTestCase(BaseTest):

    def test_successful_credit_card_validator(self):
        payload = {
            "booking_datetime": "2025-04-05 10:55:00",
            "departure_scheduled_datetime": "2025-04-17 15:25:00",
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
        cc_type = payload.get("card_type")
        validator_result = validate_credit_card_type(cc_type)
        self.assertTrue(validator_result)

    def test_fail_credit_card_validator(self):
        payload = {
            "booking_datetime": "2025-04-05 10:55:00",
            "departure_scheduled_datetime": "2025-04-17 15:25:00",
            "card_type": "Mistercard",
            "bin_number": "520275",
            "transaction_amount": 5956,
            "currency_code": "CAD",
            "source": "FLAIROCI",
            "applied_3ds": True,
            "country": "Canada",
            "departurecity": "YYZ",
            "destinationcity": "YEG"
        }
        cc_type = payload.get("card_type")
        validator_result = validate_credit_card_type(cc_type)
        self.assertFalse(validator_result)

    def test_successful_currency_code_validator(self):
        payload = {
            "booking_datetime": "2025-04-05 10:55:00",
            "departure_scheduled_datetime": "2025-04-17 15:25:00",
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
        currency_code = payload.get("currency_code")
        validator_result = validate_currency_code(currency_code)
        self.assertTrue(validator_result)

    def test_fail_currency_code_validator(self):
        payload = {
            "booking_datetime": "2025-04-05 10:55:00",
            "departure_scheduled_datetime": "2025-04-17 15:25:00",
            "card_type": "Mastercard",
            "bin_number": "520275",
            "transaction_amount": 5956,
            "currency_code": "FCFA",
            "source": "FLAIROCI",
            "applied_3ds": True,
            "country": "Canada",
            "departurecity": "YYZ",
            "destinationcity": "YEG"
        }
        currency_code = payload.get("currency_code")
        validator_result = validate_currency_code(currency_code)
        self.assertFalse(validator_result)


    def test_successful_departure_date_validator(self):
        payload = {
            "booking_datetime": "2025-04-05 10:55:00",
            "departure_scheduled_datetime": "2025-04-17 15:25:00",
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
        # Get current datetime and add one day
        future_time = datetime.now() + timedelta(days=1)
        validator_result = validate_departure_date(future_time.strftime("%Y-%m-%d %H:%M:%S"))
        self.assertTrue(validator_result)

    def test_fail_departure_date_validator(self):
        payload = {
            "booking_datetime": "2025-04-05 10:55:00",
            "departure_scheduled_datetime": "2025-04-14 15:25:00",
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
        departure_date = payload.get("departure_scheduled_datetime")
        with self.assertRaises(ValueError):
            validate_departure_date(departure_date)
       # self.assertRaises(ValueError)

    def test_successful_source_validator(self):
        payload = {
            "booking_datetime": "2025-04-05 10:55:00",
            "departure_scheduled_datetime": "2025-04-14 15:25:00",
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
        source = payload.get("source")
        validator_result = validate_source(source)
        self.assertTrue(validator_result)

    def test_fail_source_validator(self):
        payload = {
            "booking_datetime": "2025-04-05 10:55:00",
            "departure_scheduled_datetime": "2025-04-14 15:25:00",
            "card_type": "Mastercard",
            "bin_number": "520275",
            "transaction_amount": 5956,
            "currency_code": "CAD",
            "source": "FLAIROC",
            "applied_3ds": True,
            "country": "Canada",
            "departurecity": "YYZ",
            "destinationcity": "YEG"
        }
        source = payload.get("source")
        validator_result = validate_source(source)
        self.assertFalse(validator_result)
