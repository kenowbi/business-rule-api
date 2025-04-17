

def validate_credit_card_type(cc_type: str) -> bool:
    accepted_cc_types= ["Mastercard","Mastercard Debit","Visa","Visa Debit"]
    if cc_type in accepted_cc_types:
        return True
    return False


