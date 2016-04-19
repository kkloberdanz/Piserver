import RPi.GPIO as GPIO

def flip_light(light_id, choice):
    # pin_number = int(light_id) + 11
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
    else:
        print('only valid choices are ON and OFF (case insensitive)')


