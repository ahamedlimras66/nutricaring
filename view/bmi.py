from flask import render_template

class Bmi:
    def bmiPage(self):
        return render_template("bmi.html")