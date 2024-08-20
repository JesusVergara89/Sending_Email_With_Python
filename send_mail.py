import smtplib
import os
from dotenv import load_dotenv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


load_dotenv()

sender = os.getenv('user')

send_to = 'jesusmanuelv1989@gmail.com'
topic = 'test'

msg = MIMEMultipart()
msg['subject'] = topic
msg['from'] = sender
msg['To'] = send_to
with open('email.html','r') as file:
    html = file.read()

msg.attach(MIMEText(html, 'html'))

server = smtplib.SMTP('smtp.gmail.com', 587)

server.starttls()
server.login(sender, os.getenv('pass'))

server.sendmail(sender,send_to,msg.as_string())

server.quit()

