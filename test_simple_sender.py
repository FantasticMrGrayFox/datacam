import telebot
import datetime

tb = telebot.TeleBot(token="1412544928:AAERoGWd3jwaLt9RpduLScw4ToyNIdCPkVE", parse_mode=None)

def save_log(arg):
    f = open("logs/test_sender.txt", "a")
    f.write(str(datetime.datetime.now()) + " " +str(arg) + "\n\n")
    f.close()
    return

def send_p(media):
    try:
        tb.send_photo(1381883495, media ,"test")
    except Exception as Argument:
        save_log(Argument)

def send_v(media):
    try:
        tb.send_video(1381883495, media," ","test")
    except Exception as Argument:
        save_log(Argument)
    