from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
# from django.http import *
from .models import Lights

# Create your views here.
def index(request):
    # testing HTTP requests
    print("request method: ", request.method)
    print(request.GET)

    latest_lights_list = Lights.objects.order_by('-pub_date')[:5]
    # output = ', '.join([l.light_text for l in latest_lights_list])
    # template = loader.get_template('piserver.index.html')
    latest_lights_list = Lights.objects.order_by('-pub_date')[:5]
    context = { 'latest_lights_list': latest_lights_list, }
    # return HttpResponse(output)
    # return HttpResponse("Hello, and welcome to my piserver")
    # return HttpResponse(template.render(context, request))
    return render(request, 'piserver/index.html', context)

def detail(request, light_id):
    return HttpResponse("You're looking at light %s." % light_id)

def results(request, light_id):
    response = "You're looking at the results of light %s."
    return HttpResponse(response % light_id)

def flip(request, light_id):
    return HttpResponse("You're fliping light %s." % light_id)
