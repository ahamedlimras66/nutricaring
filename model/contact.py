from flask import render_template

class Contact:
    def contactPage(self):
        return render_template("contact.html")