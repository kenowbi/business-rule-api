from flask import request, jsonify
from app.business_rule_processor import processor
import logging

def determine_processor():
    json_payload = request.get_json(force=True)
    logging.info(f"Received payment request: {json_payload}")
    if not json_payload:
        return jsonify({"error": "Missing JSON payload"}), 400

    resp = processor.make_decision(json_payload)
    return jsonify({"status": "success", "data": resp}), 200