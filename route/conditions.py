from flask import Blueprint
from view.conditions import Conditions

conditions = Blueprint("conditions", __name__)

conditionsObj = Conditions()

conditions.add_url_rule("/", view_func=conditionsObj.conditionsPage, methods=['GET'])