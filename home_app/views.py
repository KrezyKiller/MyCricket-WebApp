from django.shortcuts import render
from pycricbuzz import Cricbuzz
import json
import requests
c = Cricbuzz()


def home(request):
    url =  "http://mapps.cricbuzz.com/cbzios/match/" + '20209' + "/commentary"
    list = requests.get(url).json()
    # list = json.dumps(matches,indent=4)
    # list = [10,20,20,45,70]
    send = {'matches':list}
    print(type(list))
    return render(request, 'home_app/home.html', send)
