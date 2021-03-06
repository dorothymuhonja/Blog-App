from flask_mail import Message
from flask import render_template
from . import mail

def mail_message(subject,template,to, **kwargs):
    sender_email='dmuhonja97@gmail.com'

    email = Message(subject,sender= sender_email, recipient=[to])
    email.body = render_template(template + '.txt', **kwargs)
    email.html = render_template(template + '.html', **kwargs)
    email.send(email)