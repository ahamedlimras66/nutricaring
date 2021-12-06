from flask import render_template, request

class Home:
    def homePage(self):
        return render_template("home.html")
