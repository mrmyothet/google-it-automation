#!/usr/bin/env python3

import email.message
import sys
import datetime
import email
import smtplib
import csv


def usage():
    print("send_reminders: Send meeting reminders")
    print()
    print("invocation:")
    print("    send_reminders 'date|Meeting Title|Emails' ")
    return 1


def dow(date):
    dateobj = datetime.datetime.strptime(date, r"%Y-%m-%d")
    return dateobj.strftime("%A")


def message_template(date, title):
    message = email.message.EmailMessage()
    weekday = dow(date)
    message["Subject"] = f'Meeting reminder: "{title}"'
    message.set_content(
        f"""
Hi all!
                        
This is a quick mail to remind you all that we have a meeting about:
"{title}
the {weekday} {date}.

See u there.
"""
    )
    return message


def get_name(contacts, email):
    name = ""
    with open(contacts) as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if row[0] == email:
                name = row[1]
    return name


def send_message(date, title, emails, contacts):
    smtp = smtplib.SMTP("localhost:8025")

    print(emails)

    for email in emails.split(","):
        name = get_name(contacts, email)
        message = message_template(date, title, name)
        message["From"] = "myothet@solidplm.com"
        message["To"] = email
        smtp.send_message(message)
    smtp.quit()
    pass


def main():
    if len(sys.argv) < 2:
        return usage()

    try:
        date, title, emails = sys.argv[1].split("|")
        message = message_template(date, title)
        send_message(message, emails)
        print("Successfully sent reminders to:", emails)
    except Exception as e:
        # print("Failure to send email", file=sys.stderr)
        print("Failure to send email: {}".format(e), file=sys.stderr)


if __name__ == "__main__":
    sys.exit(main())
