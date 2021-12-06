from flask import Blueprint
from view.diet import Diet

diet = Blueprint("diet", __name__)

dietObj = Diet()

diet.add_url_rule("/", view_func=dietObj.dietPage, methods=['GET'])
diet.add_url_rule("/data/", view_func=dietObj.storeData, methods=['get'])
