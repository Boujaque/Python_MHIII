# 14 - Sending Emails
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


# smtp = smtplib.SMTP(host="smtp.gmail.com", port=587)
# smtp.close()

# better with 'with' statement
with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()  # starting with "hello" message
    smtp.starttls()  # put smtp connexion in tls mode (transport layer security) that will encript al the comands sent to smtp server
    smtp.login("test.boujaque@gmail.com", "Google_1234")
    smtp.send_message(message)
    print("Sent...")
