import hou
import os
from email.message import EmailMessage
import ssl
import smtplib
import json

# Reference to hda
node = hou.pwd().parent().parent()

# Get data from parameters
email_sender = node.parm("email_sender").evalAsString()
email_reciver = node.parm("email_reciver").evalAsString()
subject = node.parm("subject").evalAsString()
body = node.parm("body").evalAsString()
password_path = node.parm("password_path").evalAsString()

# Obtain password from json file
open_file = open(password_path)
content = json.load(open_file)
password = content["password"]

# Create the email message
em = EmailMessage()
em["From"] = email_sender
em["To"] = email_reciver
em["Subject"] = subject
em.set_content(body)

# Get the file path for the attachment from the HDA parameters
file_path = node.parm("outputfilepath").evalAsString()

# Check if the attachment is enabled and attach the file if so
if node.parm("attach_video").eval()==1:
    with open(file_path, "rb") as file:
        file_data = file.read()
        file_name = os.path.basename(file_path)
    em.add_attachment(file_data, maintype="application", subtype="octet-stream", filename=file_name)

# Create a secure SSL context and send the email
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com",465,context = context) as smtp:
        smtp.login(email_sender, password)
        smtp.sendmail(email_sender,email_reciver.split(","),em.as_string())