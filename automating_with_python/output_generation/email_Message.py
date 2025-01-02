from email.message import EmailMessage

message = EmailMessage()

sender = "mr.myothet@gmail.com"
recipient = "myothet@solidplm.com"

message["From"] = sender
message["To"] = recipient

message["Subject"] = "Greetings from {} to {}!".format(sender, recipient)

body = """Hey there!

I'm learning to send emails using Python!"""

message.set_content(body)

print(message)
