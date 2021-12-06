from flask import render_template,request
from db import db
from models.schema import Users
gmail = "mm4.muthumani@gmail.com"
class Diet:
    def dietPage(self):
        return render_template("diet.html")
        
    def storeData(self):
        from app import mail, Message
        name=request.args.get('name')
        phone=request.args.get('phone')
        age=request.args.get('age')
        gender=request.args.get('gender')
        reasons=request.args.get('reasons')
        address=request.args.get('address')

        userObj = Users(full_name=name,phone=phone,age=age,gender=gender,reason=reasons,address=address)
        db.session.add(userObj)
        db.session.commit()

        msg = Message("NUTRI CARING", sender="arrowmail", recipients=[gmail])
        msg.html = render_template(
            "mail.html",
            name=name,
            mail=gmail,
            option=reasons,
            number=phone,
            address=address
            )
        mail.send(msg)