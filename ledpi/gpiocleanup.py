import RPi.GPIO as GPIO
GPIO.setwarnings(False)

GPIO.setmode(GPIO.BOARD)

GPIO.setup(12, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(18, GPIO.OUT) 

GPIO.output(12, GPIO.LOW)
GPIO.output(16, GPIO.LOW)
GPIO.output(18, GPIO.LOW)

GPIO.cleanup()
