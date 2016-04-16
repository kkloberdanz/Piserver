from django.shortcuts import render
# from django.http import HttpResponse, HttpRequest
from django.http import *

# Create your views here.
def index(request):
    print("request method: ", request.method)
    print(request.GET)
    return HttpResponse("Hello, and welcome to my piserver")
