from flask import render_template

class Meal:
    def mealPage(self):
        return render_template("meal.html")