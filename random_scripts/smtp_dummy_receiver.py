import smtpd
import asyncore
import time


class CustomSMTPServer(smtpd.SMTPServer):

    def process_message(self, peer, mailfrom, rcpttos, data, mail_options=None, rcpt_options=None):
        print('Receiving message from:', peer)
        print('Message addressed from:', mailfrom)
        print('Message addressed to  :', rcpttos)
        print('Message length        :', len(data))

        filename = 'raw_emails/raw_email_' + str(int(time.time())) + '.txt' 

        with open(filename, 'wb') as fp: 
            fp.write(data)


server = CustomSMTPServer(('127.0.0.1', 1025), None)

asyncore.loop()