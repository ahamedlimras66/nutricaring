from flask import Blueprint
from view.meal import Meal

meal = Blueprint("meal", __name__)

mealObj = Meal()

meal.add_url_rule("/", view_func=mealObj.mealPage, methods=['GET'])