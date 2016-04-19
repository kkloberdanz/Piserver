from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
# from django.http import *
from django.core.urlresolvers import reverse
from django.views import generic
from .models import Lights, Choice
from django.middleware.csrf import get_token

import RPi.GPIO as GPIO
from .lights import *


# Create your views here.
@csrf_exempt
def index(request):

    latest_lights_list = Lights.objects.order_by('-pub_date')[:5]
    # output = ', '.join([l.light_text for l in latest_lights_list])
    # template = loader.get_template('piserver.index.html')
    latest_lights_list = Lights.objects.order_by('-pub_date')[:5]
    context = { 'latest_lights_list': latest_lights_list, }
    # return HttpResponse(output)
    # return HttpResponse("Hello, and welcome to my piserver")
    # return HttpResponse(template.render(context, request))
    return render(request, 'piserver/index.html', context)

@csrf_exempt
def detail(request, light_id): 
    # return HttpResponse("You're looking at light %s." % light_id)
    light = get_object_or_404(Lights, pk=light_id)
    return render(request, 'piserver/detail.html', {'light':light})

@csrf_exempt
def results(request, light_id):
    light = get_object_or_404(Lights, pk=light_id)    
    # response = "You're looking at the results of light %s."
    # return HttpResponse(response % light_id)
    return render(request, 'piserver/results.html', {'light':light})

@csrf_exempt
def flip(request, light_id):
    # csrf_token = get_token(request)
    # request.META["CSRF_COOKIE_USED"] = True
    if request.method == 'POST':
        print('here!!!!')
        print("POST dict:", request.POST)

    light = get_object_or_404(Lights, pk=light_id)

    # testing HTTP requests
    print("request method: ", request.method)
    print("GET dict:", request.GET)
    print("POST dict:", request.POST)
    try:
        selected_choice = light.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'piserver/detail.html', {
            'light': light,
            'error_message': "You didn't select a choice.",
        })
    else:
        # print(type(selected_choice.choice_text))
        if selected_choice.choice_text == "Off":
            selected_choice.on = 0
        else:
            selected_choice.on = 1

        flip_light(light_id, selected_choice.choice_text)
        selected_choice.save()
        print("light: ", light_id, " is now ", end='') 
        # outfile = open("lightValues", "w")
        if selected_choice.on:
            print("On")
            # outfile.write(str(1))
        else:
            print("Off")
            # outfile.write(str(0))
        # outfile.close()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('piserver:results', args=(light.id,)))    
    # return HttpResponse("You're fliping light %s." % light_id)
