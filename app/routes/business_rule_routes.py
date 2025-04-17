from flask import Blueprint
from app import rest
from app.configs.Config import Config

rules_blueprint = Blueprint(Config.RULES_BLUEPRINT_NAME,__name__)
rules_blueprint.route(Config.BUSINESS_RULES_ENDPOINT,methods=['POST'])(rest.determine_processor)