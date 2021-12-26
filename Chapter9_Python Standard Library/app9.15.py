# 15 - Templates
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from pathlib import Path
import smtplib

message = MIMEMultipart()
message["from"] = "Mosh Hamedani"
message["to"] = "rafael.constantinescu@gmail.com"
message["subject"] = "this is a test"
message.attach(MIMEText("Body", "plain"))
message.attach(MIMEImage(Path(
    r"C:\Users\rafae\Pictures\Saved Pictures\Beautiful Scenery Desktop Wallpapers - Top Free Beautiful Scenery Desktop Backgrounds - WallpaperAccess_files\1637.jpg").read_bytes()))


with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()  
    smtp.starttls()  
    smtp.login("email@adress", "password")
    smtp.send_message(message)
    print("Sent...")
