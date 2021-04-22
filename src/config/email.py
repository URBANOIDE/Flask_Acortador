from flask import Flask
from flask_mail import Mail, Message
import os

app = Flask(__name__)
nombre = "Albertochind04@gmail.com"
password = "NubiaUrban0"

mail_settings = {
    "MAIL_SERVER": 'smtp.gmail.com',
    "MAIL_PORT": 465,
    "MAIL_USE_TLS": False,
    "MAIL_USE_SSL": True,
    "MAIL_USERNAME": nombre,
    "MAIL_PASSWORD": password
}

app.config.update(mail_settings)
mail = Mail(app)

def verificar_email():
    with app.app_context():
        msg = Message(subject="Hello",
            sender=app.config.get("MAIL_USERNAME"),
            recipients=[nombre], # replace with your email for testing
            body="http://127.0.0.1:5000")
        mail.send(msg)