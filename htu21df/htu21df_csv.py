# A simple program to test the driver

import time
import datetime
import HTU21DF

def writecsv(c, rh):
    import csv
    with open('eggs.csv', 'a') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
        now = datetime.datetime.fromtimestamp(time.time).strftime('%Y-%m-%d %H:%M:%S')
        spamwriter.writerow([c,rh])
        csvfile.close

while True:
    #print("sending reset...")
    HTU21DF.htu_reset
    temperature = HTU21DF.read_temperature()
    print("The temperature is %3.2f C." % round(temperature, 2))
    time.sleep(1)
    humidity = HTU21DF.read_humidity()
    print("The humidity is %3.2f %%rh." % round(humidity, 2))
    #writecsv(temperature, humidity)
    time.sleep(60)

