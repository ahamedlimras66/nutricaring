from flask import Flask, url_for
from flask_cors import CORS, cross_origin
from route.home import home
from route.about import about
from route.bmi import bmi
from route.contact import contact
from route.diet import diet

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

app.register_blueprint(home, url_prefix="/")
app.register_blueprint(about, url_prefix="/about")
app.register_blueprint(bmi, url_prefix="/bmi/")
app.register_blueprint(contact, url_prefix="/contact")
app.register_blueprint(diet, url_prefix="/diet")

if __name__ == "__main__":
    app.run(debug=True)