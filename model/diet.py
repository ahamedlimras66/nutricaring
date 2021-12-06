from flask import render_template

class Diet:
    def dietPage(self):
        return render_template("diet.html")