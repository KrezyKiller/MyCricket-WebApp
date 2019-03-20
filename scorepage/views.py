from django.shortcuts import render,HttpResponse
from home_app.views import c


def score(request, id):
   score = c.scorecard(id)
   send = {'data':score}
   print(score['scorecard'])
   return render(request, 'score/score.html', send)
