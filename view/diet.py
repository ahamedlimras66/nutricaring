from flask import render_template,request,send_from_directory
from db import db
import os
from models.schema import Users
from models.report import Report

gmail = "limraslim@gmail.com"
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
        weight=request.args.get('weight')
        height=request.args.get('height')

        userObj = Users(full_name=name,phone=phone,age=age,gender=gender,reason=reasons,address=address,weight=weight,height=height)
        db.session.add(userObj)
        db.session.commit()

        msg = Message("NUTRI CARING", sender="arrowmail", recipients=[gmail])
        msg.html = render_template(
            "mail.html",
            name=name,
            mail=gmail,
            option=reasons,
            number=phone,
            address=address,
            weight=weight,
            height=height
            )
        mail.send(msg)

        reportObj = Report(
            name=name,
            phoneNumber=phone,
            address=address,
            reason=reasons,
            weight=weight,
            height=height
        )
        reportObj.make()
        workingdir = os.path.abspath(os.getcwd())
        print(weight,height)
        return send_from_directory(workingdir, reportObj.reportFile)
