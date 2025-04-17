from flask import Flask
import logging
from app import routes


def create_app():
    app = Flask(__name__)
    app.register_blueprint(routes.rules_blueprint)#, url_prefix="/rules"
    # Logging
    logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s')
    return app