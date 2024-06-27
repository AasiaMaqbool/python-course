import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email=EmailMessage()
email['from']='Aasia Maqbool'
email['to']='usmannaveed13@gmail.com'
email['subject']= 'yor are lucky to have me as a wife'

email.set_content(html.substitute({'name': 'tintin'}))

with smtplib.SMTP(host='smtp.gmail.com',port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('aasimaqbool@gmail.com','hsae eert sjep izxf')
    smtp.send_message(email)
    print('all good boss!')