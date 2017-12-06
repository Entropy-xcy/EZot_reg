import smtplib
import email
import os

USERNAME = os.environ.get("EZOT_EMAIL_USERNAME")
PASSWD = os.environ.get("EZOT_EMAIL_PASSWD")
SMTP_SERVER = os.environ.get("SMTP_SERVER")


def send_email_to(email_addr, subject, content):
    msg = email.message_from_string(content)
    msg['From'] = USERNAME
    msg['To'] = email_addr
    msg['Subject'] = subject

    s = smtplib.SMTP(SMTP_SERVER, 587)
    s.ehlo()  # Hostname to send for this command defaults to the fully qualified domain name of the local host.
    s.starttls()  # Puts connection to SMTP server in TLS mode
    s.ehlo()
    s.login(USERNAME, PASSWD)
    s.sendmail(USERNAME, email_addr, msg.as_string())
    s.quit()


def main():
    send_email_to("entropy.xcy@hotmail.com", "Hello World!!", "Hello Worlaasdfasdfasdfd!!")


if __name__ == "__main__":
    main()
