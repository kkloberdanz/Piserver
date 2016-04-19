import RPi.GPIO as GPIO

def light1_on(): 
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(12, GPIO.OUT)
    GPIO.output(12, GPIO.HIGH)

def light1_off(): 
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(12, GPIO.OUT)
    GPIO.output(12, GPIO.LOW) 

