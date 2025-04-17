
def validate_currency_code(currency_code: str) -> bool:
    accepted_currency_codes = ["CAD", "USD"]
    if currency_code in accepted_currency_codes:
        return True
    return False