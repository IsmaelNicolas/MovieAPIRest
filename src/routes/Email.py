from flask import Blueprint,jsonify,request
from decouple import config 
from email.message import EmailMessage
import ssl
import smtplib

main = Blueprint('email_blueprint',__name__)

@main.route("/welcome",methods=['POST'])
def send_email_welcome():
    try:
        email_from = "nicolas.nxd@gmail.com"
        email_key = config('EMAIL_KEY')
        email_to = request.json['email']

        subject = "Welcome to Cinect TM"
        body = "welcome to Cinect TM"

        em = EmailMessage()
        em['from'] = email_from
        em['to'] = email_to
        em['subject'] = subject
        em.set_content(body)

        context = ssl.create_default_context()

        with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context)as smtp:
            smtp.login(user=email_from,password=email_key)
            smtp.sendmail(email_from,email_to,em.as_string())

        return jsonify({'message':'Email send'})    


    except Exception as e:
        return jsonify({'message':str(e)})
