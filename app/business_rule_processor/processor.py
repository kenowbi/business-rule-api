from app.services.business_rule_service import BusinessRuleService
import logging

def make_decision(json_data):
    # call your service
    rule_service = BusinessRuleService(json_data=json_data)
    result = rule_service.determine_processor()
    logging.info(f"Final Result: {result}")
    if result:
        return "Elavon"
    return "No available processor"