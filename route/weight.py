from flask import Blueprint
from view.weight import Weight

weight = Blueprint("weight", __name__)

weightObj = Weight()

weight.add_url_rule("/", view_func=weightObj.weightPage, methods=['GET'])