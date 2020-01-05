import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

def my_callback(channel):
	print('You pressed the button')
	
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(4, GPIO.FALLING, callback=my_callback)

for i in range(5):
	time.sleep(1)

print(i)
GPIO.cleanup()		
	
