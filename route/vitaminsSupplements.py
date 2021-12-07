from flask import Blueprint
from view.vitaminsSupplements import VitaminsSupplements

vitaminsSupplements = Blueprint("vitaminsSupplements", __name__)

vitaminsSupplementsObj = VitaminsSupplements()

vitaminsSupplements.add_url_rule("/", view_func=vitaminsSupplementsObj.vitaminsSupplementsPage, methods=['GET'])