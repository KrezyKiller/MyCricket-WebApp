from django.shortcuts import render
from pycricbuzz import Cricbuzz
import json
import requests
c = Cricbuzz()


def home(request):
    matches = c.matches()
    send = {'matches' : matches}
    return render(request, 'home_app/home.html', send)

def new_home(request):
    matches = c.matches()
    send = {'matches' : matches}
    return render(request, 'home_app/new_home.html', send)
