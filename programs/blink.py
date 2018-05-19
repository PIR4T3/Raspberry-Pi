import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)

n = int(input('Times: '))
# for connection ground and pin 12
for i in range(n):
	print "Blink ",(i+1)
	GPIO.output(18,GPIO.HIGH)
	time.sleep(1)
	GPIO.output(18,GPIO.LOW)
print 'Done'
