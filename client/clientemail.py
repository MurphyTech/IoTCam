import os
import smtplib
import sys
import json
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email.mime.image import MIMEImage
from email import encoders

class Email():
    def __init__(self, filename):
        config = json.load(open('conf.json', 'r'))

        msg = MIMEMultipart()
        msg['From'] = config["fromaddr"]
        msg['To'] = config["COMMASPACE"].join(config["toaddr"])
        msg['Subject'] = "IOT Camera"

        print("[SUCCESS] - Message created...")

        msg.attach(MIMEText(config["message"],"plain"))

        attachment = open(filename, 'rb')

        part = MIMEBase('application', 'octet-stream')
        part.set_payload((attachment).read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', "attachment; filename= %s" +filename)

        print("[SUCCESS] - Image file attached...")

        msg.attach(part)
        text = msg.as_string()

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(fromaddr, 'raspberrypi')

        server.sendmail(fromaddr, toaddr, text)
        server.quit()

        print("[SUCCESS] - Message Sent...")
