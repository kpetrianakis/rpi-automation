# A simple program to test the driver

import time
import HTU21DF

success = False
while True:
	try:
		#print("sending reset...")
		HTU21DF.htu_reset
		temperature = HTU21DF.read_temperature()
		print("The temperature is %3.2f C." % round(temperature, 2))
		time.sleep(1)
		humidity = HTU21DF.read_humidity()
		print("The humidity is %3.2f %%rh." % round(humidity,2))
	        success = True
		time.sleep(60)
	except Exception as e:
            print "error: %s"%(e)
	    # wait a second for the retry
            time.sleep(1)
            success = False
	if not success:
	    print "Failed once! Retrying..."
