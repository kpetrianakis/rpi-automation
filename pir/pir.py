import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(20, GPIO.IN)         #Read output from PIR motion sensor
#GPIO.setup(3, GPIO.OUT)         #LED output pin

while True:
    time.sleep(5)
    i=GPIO.input(20)
    if i==0:                 #When output from motion sensor is LOW
        print ("No intruders",i)
        #GPIO.output(3, 0)  #Turn OFF LED
    elif i==1:               #When output from motion sensor is HIGH
        print ("Intruder detected",i)
        #GPIO.output(3, 1)  #Turn ON LED
