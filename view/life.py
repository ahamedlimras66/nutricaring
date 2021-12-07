from flask import render_template

class Life:
    def lifePage(self):
        return render_template("life.html")