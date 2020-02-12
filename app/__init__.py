from flask import Flask
from flask_mail import Mail

app = Flask(__name__)
app.config['SECRET_KEY'] = 'this is Sparta!'
app.config['MAIL_SERVER'] = 'smtp.mailtrap.io'
app.config['MAILPORT'] = '465' # 465 or 2525
app.config['MAIL_USERNAME'] = 'e08fdab99ed272'
app.config['MAIL_PASSWORD'] = 'b83b6b2e220324'

mail = Mail(app)
from app import views