from email.message import EmailMessage
import os.path
import mimetypes
import smtplib
import getpass

message = EmailMessage()

sender = "myothet@solidplmtech.com"
recipient = "myothet@solidplm.com"

message["From"] = sender
message["To"] = recipient

message["Subject"] = "Greetings from {} to {}!".format(sender, recipient)

body = """Hey there!

I'm learning to send emails using Python!



Best Regards, 
Myo Thet 
"""

message.set_content(body)

attachment_path = "./temp/education.png"
attachment_filename = os.path.basename(attachment_path)

mime_type, _ = mimetypes.guess_type(attachment_path)
mime_type, mime_subtype = mime_type.split("/", 1)
# print(mime_type, mime_subtype)

with open(attachment_path, "rb") as ap:
    message.add_attachment(
        ap.read(),
        maintype=mime_type,
        subtype=mime_subtype,
        filename=os.path.basename(attachment_path),
    )

# print(message)

mail_server = smtplib.SMTP_SSL("mail5009.site4now.net", 465)
mail_server.set_debuglevel(1)

mail_password = getpass.getpass(prompt="Password? ")

try:
    mail_server.login(sender, mail_password)
    mail_server.send_message(message)
except smtplib.SMTPAuthenticationError:
    print("SMTP Authentication Error")
finally:
    mail_server.quit()
