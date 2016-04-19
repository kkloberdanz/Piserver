import requests

def flip_light(light, position, webpage, intensity=100):
    # url = 'http://192.168.0.7:8000/piserver/' + str(light) + '/flip/'
    url = webpage + str(light) + '/flip/'
    if position == "off":
        choice = str(2)
    elif position == "on":
        choice = str(1)
    else:
        print("flip_light: only options are \'on\' and \'off\'")
    # command = str(", {\'choice\':[\'" + choice + "\']}")
    requests.post(url, {'choice':[choice]})

