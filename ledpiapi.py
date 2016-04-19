import requests
def turn_off(light):
    url = "http://192.168.0.5:8000/piserver/" + str(light) + "/flip"
    selection = ", {'choice':['1']}"
    requests.post(url+selection)

def turn_on(light):
    url = "http://192.168.0.5:8000/piserver/" + str(light) + "/flip"
    selection = ", {'choice':['2']}"
    requests.post(url+selection)

