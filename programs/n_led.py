import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)

print 'Press 1:RED  2:GREEN  3: BOTH\n'

ip = int(input('LED: '))

# for red connection ground and pin 11
if ip == 1:
	print 'RED\n'
	GPIO.output(17,GPIO.HIGH)
	time.sleep(3)
	GPIO.output(17,GPIO.LOW)

# for green connection ground and pin 12
if ip == 2:
        print 'GREEN\n'
        GPIO.output(18,GPIO.HIGH)
        time.sleep(3)
        GPIO.output(18,GPIO.LOW)

if ip == 3:
        print 'All\n'
        GPIO.output(17,GPIO.HIGH)
        GPIO.output(18,GPIO.HIGH)
	time.sleep(3)
        GPIO.output(17,GPIO.LOW)
	GPIO.output(18,GPIO.LOW)
print 'Done'
