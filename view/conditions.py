from flask import render_template

class Conditions:
    def conditionsPage(self):
        return render_template("conditions.html")