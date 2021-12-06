from flask import Blueprint
from model.about import About

about = Blueprint("about", __name__)

aboutObj = About()

about.add_url_rule("/", view_func=aboutObj.aboutPage, methods=['GET'])