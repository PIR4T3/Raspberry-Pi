#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

RelayPin = 11    # pin11

def setup():
	GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
	GPIO.setup(RelayPin, GPIO.OUT)
	GPIO.output(RelayPin, GPIO.LOW)

def loop():
	while (1):
		ip = int(input("IP: "))
	
		if ip==1:
			print 'ON\n'
			GPIO.output(RelayPin, GPIO.HIGH)
        		time.sleep(1)

		elif ip==0:
        		print 'OFF\n'
        		GPIO.output(RelayPin, GPIO.LOW)
        		time.sleep(1)

def destroy():
	GPIO.output(RelayPin, GPIO.HIGH)
	GPIO.cleanup()                     # Release resource

if __name__ == '__main__':     # Program start from here
	setup()
	try:
		loop()
	except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
		destroy()


