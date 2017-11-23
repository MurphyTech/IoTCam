
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
    def __init__(self, imagefile):

        config = json.load(open("client/config.json", 'r'))

        msg = MIMEMultipart()
        msg['From'] = config["fromaddr"]
        msg['To'] = config["COMMASPACE"].join(config["toaddr"])
        msg['Subject'] = "IOT Camera"

        print("[SUCCESS] - Message created...")

        msg.attach(MIMEText(config["message"],"plain"))
	imagefile = imagefile[2:len(imagefile)]
	wd = "/home/pi/IoTCam/IoTCam"
	filename = wd + imagefile
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
        server.login(config["fromaddr"], 'raspberrypi')

        server.sendmail(config["fromaddr"],config["toaddr"], text)
        server.quit()

        print("[SUCCESS] - Message Sent...")
