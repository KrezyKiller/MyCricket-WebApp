from django.shortcuts import render
from pycricbuzz import Cricbuzz
import json
import requests
c = Cricbuzz()


def home(request):
    matches = c.matches()
    send = {'matches' : matches}
    print(matches)
    return render(request, 'home_app/home.html', send)
