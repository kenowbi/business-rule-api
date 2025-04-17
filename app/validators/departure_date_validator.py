from datetime import datetime
import logging

def validate_departure_date(departure_date_str: str) -> bool:
    if not departure_date_str:
        logging.info(f"Departure Date: {departure_date_str}")
        raise ValueError("Departure Date must be present.")
    departure_date =""
    try:
        departure_date = datetime.strptime(departure_date_str, "%Y-%m-%d %H:%M:%S")
    except ValueError as err:
        print(err.args)
    if datetime.now() > departure_date:
        logging.info(f"Departure date lies in the past: {departure_date}")
        raise ValueError("Departure date lies in the past")
    return True

