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
outer = MIMEMultipart()
#msg = MIMEText('5\n2020-10-19 13:01:00.300\n23\n Hola mundo ', _subtype='plain') #Cambiare el renglon por otro indicador para intentar la funcion split
msg = MIMEText('|23|Hola mundo ', _subtype='plain')
outer.attach(msg)

outer['Subject'] = 'Camera Alert - Motion Detection'
outer['To'] = email.utils.formataddr(('Recipient', 'recipient@example.com'))
outer['From'] = email.utils.formataddr(('Author', 'author@example.com'))
outer.preamble = 'You will not see this in a MIME-aware mail reader.\n'

subtype = 'octet-stream'
filename = 'alert-cam-1.jpg'
fp = open(filename, 'rb')
msg = MIMEImage(fp.read(), _subtype=subtype)
msg.add_header('Content-Disposition', 'attachment', filename= f'sent-{filename}')
outer.attach(msg)

# msg.add_attachment(img_data, maintype='image', subtype=imghdr.what(None, img_data))

server = smtplib.SMTP(host, port)
server.set_debuglevel(True)  # show communication with the server

try:
    # server.login(username, password)
    server.sendmail('author@example.com',
                    ['recipient@example.com'],
                    outer.as_string())
finally:
    server.quit()

