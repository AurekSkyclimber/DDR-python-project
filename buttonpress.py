import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(20, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP)



def red():
        input_red = GPIO.input(18)
        if input_red == False:
        	print('Red Button Pressed')
		return 1
	else:
		print('Red Button Missed')
       		return -1
        
def green():
        input_green = GPIO.input(17)
        if input_green == False:
        	print('Green Button Pressed')
		return 1
	else:
		print('Green Button Missed')
		return -1
        
def yellow():
        input_yellow = GPIO.input(20)
        if input_yellow == False:
        	print('Blue Button Pressed')
		return 1
	else:
		print('Blue Button Missed')
		return -1
	
def blue():
        input_blue = GPIO.input(21)
        if input_blue == False:
        	print('Yellow Button Pressed')
		return 1
	else:
		print('Yellow Button Missed')
		return -1