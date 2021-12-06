from flask import render_template

class About:
    def aboutPage(self):
        return render_template("about.html")