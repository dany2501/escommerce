from rest.controller.Controller import Controller
from cerberus.responses.BodyRS import BodyRS
from cerberus.responses.HeaderRS import HeaderRS
from cerberus.responses.Response import Response
from flask_mail import Message
from app import mail
from jinja2 import Template
from datetime import datetime
from app import app

class EmailService(Controller):

    """docstring for EmailService"""
    def __init__(self):
        super(EmailService, self).__init__()
    def sendEmailClient (self,recipient,code,name):
        msg = Message(subject="Verificar Correo Escommerce",
                      sender=app.config.MAIL_USERNAME,
                      recipients=[recipient], # replace with your email for testing
                      html="""<h1>Bienvenid@ a <strong>Escommerce</strong></h1><br>
                      <h3>¡Hola! """+name+"""</h3><br><p>Tu cuenta está casi lista. Únicamente ingresa tu código y verifica tu correo!</p>
                        <br><p>Tu código de verificación es: """+str(code)+"""
                      """)
        mail.send(msg)