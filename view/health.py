from flask import render_template

class Health:
    def healthPage(self):
        return render_template("health.html")