import RPi.GPIO as GPIO
import time

def flip_light(light_id, choice):
    GPIO.setwarnings(False)

    if light_id == '1':
        pin_number = 12

    elif light_id == '2':
        pin_number = 16

    elif light_id == '3':
        pin_number = 18

    GPIO.setmode(GPIO.BOARD) 
    GPIO.setup(pin_number, GPIO.OUT)

    if choice.upper() == 'OFF':
        GPIO.output(pin_number, GPIO.LOW)

    elif choice.upper() == 'ON':
        GPIO.output(pin_number, GPIO.HIGH)

    elif choice.upper() == 'HALF':
        p = GPIO.PWM(pin_number, 50)
        p.start(0) 
        p.ChangeDutyCycle(50)
        time.sleep(1)
        GPIO.output(pin_number, GPIO.HIGH)

    elif choice.upper() == 'QUARTER':
        p = GPIO.PWM(pin_number, 50)
        p.start(0) 
        p.ChangeDutyCycle(25)
        time.sleep(1)
        GPIO.output(pin_number, GPIO.HIGH)

    else: 
        print('only valid choices are ON, OFF, HALF, QUARTER (case insensitive)')

