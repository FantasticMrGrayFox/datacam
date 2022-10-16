import time
import os


while True:
    os.system("sudo systemctl status datacam_smtp.service")
    os.system("sudo systemctl status datacam_app.service")
    os.system("sudo systemctl status datacam_telbot.service")
    time.sleep(1.800)







