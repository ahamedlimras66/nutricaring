from flask import Blueprint
from view.life import Life

life = Blueprint("life", __name__)

lifeObj = Life()

life.add_url_rule("/", view_func=lifeObj.lifePage, methods=['GET'])