from flask import Blueprint
from view.health import Health

health = Blueprint("health", __name__)

healthObj = Health()

health.add_url_rule("/", view_func=healthObj.healthPage, methods=['GET'])