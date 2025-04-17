from datetime import datetime
import logging

from app.validators.departure_date_validator import validate_departure_date
from app.validators.source_validator import validate_source


def calculate_day_difference(date_str: str) -> int:
    # Parse the input string to a datetime object
    try:
        if not validate_departure_date(date_str):
            raise ValueError("Invalid Departure Date")
        else:
            departure_date = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
            logging.info(f"Target Date: {departure_date}")
            # Get the current datetime
            now = datetime.now()
            # Calculate the difference in days
            difference = departure_date - now
            return difference.days
    except ValueError:
        raise ValueError("Date must be in the format 'YYYY-MM-DD HH:MM:SS'")


class BusinessRuleService:

    def __init__(self, json_data):
        self.json_data = json_data


    def determine_processor(self):
        if self.flight_rule() and self.three_ds_validation_rule() and self.purchasing_location_rule():
            return True
        return False

    # @staticmethod

    def flight_rule(self):
        departure_date = self.json_data["departure_scheduled_datetime"]
        difference_in_days = calculate_day_difference(departure_date)
        logging.info(f"Date difference: {difference_in_days}")

        if difference_in_days < 0:
            raise ValueError("Invalid date")
        return True

    # @staticmethod
    def three_ds_validation_rule(self):
        three_ds_applied = self.json_data["applied_3ds"]
        if not three_ds_applied:
            return False
        return True

    # @staticmethod
    def purchasing_location_rule(self):
        purchasing_location = self.json_data["source"]
        return validate_source(purchasing_location)
