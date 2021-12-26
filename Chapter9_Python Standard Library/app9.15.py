# 15 - Templates
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from pathlib import Path
from string import Template
import smtplib

template = Template(Path("template.html").read.txt)
template.substitute()

message = MIMEMultipart()
message["from"] = "Mosh Hamedani"
message["to"] = "rafael.constantinescu@gmail.com"
message["subject"] = "this is a test"
# body = template.substitute({"name": "John"})
body = template.substitute(name = "John")
message.attach(MIMEText(bady, "html"))
message.attach(MIMEImage(Path(
    r"C:\Users\rafae\Pictures\Saved Pictures\Beautiful Scenery Desktop Wallpapers - Top Free Beautiful Scenery Desktop Backgrounds - WallpaperAccess_files\1637.jpg").read_bytes()))


with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()  
    smtp.starttls()  
    smtp.login("email@adress", "password")
    smtp.send_message(message)
    print("Sent...")
