import os
from models.schema import *
from flask import Flask
from route.home import home
from route.about import about
from route.bmi import bmi
from route.contact import contact
from route.diet import diet
from route.conditions import conditions
from route.health import health
from route.life import life
from route.meal import meal 
from route.vitaminsSupplements import vitaminsSupplements
from route.weight import weight
from flask_mail import Mail,Message

app = Flask(__name__)
app.secret_key = 'my-secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'nutricaringsender@gmail.com'
app.config['MAIL_PASSWORD'] = '7418106905'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

@app.before_first_request
def create_table():
    db.create_all()

app.register_blueprint(home, url_prefix="/")
app.register_blueprint(about, url_prefix="/about")
app.register_blueprint(bmi, url_prefix="/bmi/")
app.register_blueprint(contact, url_prefix="/contact")
app.register_blueprint(diet, url_prefix="/diet")
app.register_blueprint(conditions, url_prefix="/conditions")
app.register_blueprint(health, url_prefix="/health")
app.register_blueprint(life, url_prefix="/life")
app.register_blueprint(meal, url_prefix="/meal")
app.register_blueprint(vitaminsSupplements, url_prefix="/vitaminsSupplements")
app.register_blueprint(weight, url_prefix="/weight")

if __name__ == "__main__":
    from db import db
    db.init_app(app)
    app.run(debug=True)