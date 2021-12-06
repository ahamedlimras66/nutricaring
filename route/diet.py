from flask import Blueprint
from model.diet import Diet

diet = Blueprint("diet", __name__)

dietObj = Diet()

diet.add_url_rule("/", view_func=dietObj.dietPage, methods=['GET'])