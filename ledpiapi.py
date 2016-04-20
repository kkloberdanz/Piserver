import requests

def flip_light(light, position, webpage, intensity=100):
    # url = 'http://192.168.0.7:8000/piserver/' + str(light) + '/flip/'
    url = webpage + str(light) + '/flip/'
    if position.upper() == "OFF":
        if light == 1:
            choice = str(2)
        elif light == 2:
            choice = str(3)
        elif light == 3:
            choice = str(5)
        else:
            print('not a valid light')
    elif position.upper() == "ON":
        if light == 1:
            choice = str(1)
        elif light == 2:
            choice = str(4)
        elif light == 3:
            choice = str(6)
        else:
            print('not a valid light')
    else:
        print("flip_light: only options are \'on\' and \'off\'")
    # command = str(", {\'choice\':[\'" + choice + "\']}")
    requests.post(url, {'choice':[choice]})

