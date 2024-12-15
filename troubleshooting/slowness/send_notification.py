import asyncio
import smtplib
from threading import Thread
import email
import datetime
from send_reminders import message_template
from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")


# Assume a  flask restful interface endpoint
@app.route("/notify")
def notify():
    """Request notification email"""

    email = request.args["email"]
    print(email)

    # Create the new loop and worker thread
    worker_loop = asyncio.new_event_loop()
    worker = Thread(
        target=start_email_worker,
        args=worker_loop,
    )

    # Start the thread
    worker.start()

    worker_loop.call_soon_threadsafe(send_notification, email)

    return render_template("login.html")


def send_notification(email):
    """
    Generate and send the notification email
    """
    # Do some work to get email body
    message = message_template("2024-12-15", "Sending notifiction from Gmail")

    # Connect to the server
    server = smtplib.SMTP("smpt.gmail.com:587")
    server.ehlo()
    server.starttls()
    server.login(user="emeryrambo@gmail.com", password="Opensesame2025")

    # Send the email
    server.sendmail("emeryrambo@gmail.com", "mr.myothet@gmail.com", message)

    server.quit()


def start_email_worker(loop):
    """Switch to new event loop and run forever"""

    asyncio.set_event_loop(loop)
    loop.run_forever()
