import smtplib
import email.utils
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
import ssl

port = 1025  # Local test
host = '127.0.0.1'

# port = 465  # For SSL
# host = 'smtp.mailtrap.io'
# username = 'f150152345bb25'
# password = '8e7ca5200c7e20'

# Create the enclosing (outer) message

filename = 'raw_emails/raw_email_1604481889.txt'
fp = open(filename, 'rb')

server = smtplib.SMTP(host, port)
server.set_debuglevel(True)  # show communication with the server

try:
    # server.login(username, password)
    server.sendmail('DONVEGA.CAM36@datacam.lan',
                    ['recipient@example.com'],
                    fp.read())
finally:
    server.quit()

