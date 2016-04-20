import requests

def flip_light(light, position, webpage):
    # url = 'http://192.168.0.7:8000/piserver/' + str(light) + '/flip/'
    url = webpage + str(light) + '/flip/'
    if position.upper() == "OFF":
        if light == 1:
            choice = str(2)
        elif light == 2:
            choice = str(4)
        elif light == 3:
            choice = str(6)
        else:
            print('not a valid choice')

    elif position.upper() == "ON":
        if light == 1:
            choice = str(1) 
        elif light == 2:
            choice = str(3)
        elif light == 3:
            choice = str(5)
        else:
            print('not a valid choice')

    elif position.upper() == "HALF":
        if light == 1:
            choice = 7
        if light == 2:
            choice = 8
        if light == 3:
            choice = 9

    elif position.upper() == "QUARTER":
        if light == 1:
            choice = 10
        if light == 2:
            choice = 11
        if light == 3:
            choice = 12
    else:
        print("flip_light: only options are ON, OFF, HALF, and QUARTER")
    # command = str(", {\'choice\':[\'" + choice + "\']}")
    requests.post(url, {'choice':[choice]})

