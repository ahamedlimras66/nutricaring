from flask import Blueprint
from view.bmi import Bmi

bmi = Blueprint("bmi", __name__)

bmiObj = Bmi()

bmi.add_url_rule("/", view_func=bmiObj.bmiPage, methods=['GET'])