from flask import Blueprint
from model.contact import Contact

contact = Blueprint("contact", __name__)

contactObj = Contact()

contact.add_url_rule("/", view_func=contactObj.contactPage, methods=['GET'])