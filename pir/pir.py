import RPi.GPIO as GPIO
import time
from datetime import datetime

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(20, GPIO.IN)         #Read output from PIR motion sensor
#GPIO.setup(3, GPIO.OUT)         #LED output pin

def send_email(user, pwd, recipient, subject, body):
    import smtplib

    FROM = user
    TO = recipient if isinstance(recipient, list) else [recipient]
    SUBJECT = subject
    TEXT = body

    # Prepare actual message
    message = """From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(user, pwd)
        server.sendmail(FROM, TO, message)
        server.close()
        print ('successfully sent the mail')
    except Exception as e:
        print ("failed to send mail")
        print(e)
time.sleep(60)        
while True:
    i=GPIO.input(20)
    if i==1:
        
        current_time = datetime.now().strftime("%H:%M:%S")
        print("Current Time =", current_time)
        print "Intruder detected"
        send_email('kpetrianakis@gmail.com','blgxtqnyboyngpka','kpetrianakis@gmail.com','Someone moved','now')
        time.sleep(10)
#    if i==0:                 #When output from motion sensor is LOW
#        print ("No intruders",i)
        #GPIO.output(3, 0)  #Turn OFF LED
    elif i==1:               #When output from motion sensor is HIGH
        print ("Intruder detected",i)
        send_email('kpetrianakis@gmail.com','xxxx','kpetrianakis@gmail.com','Someone moved','now')
        #GPIO.output(3, 1)  #Turn ON LED
