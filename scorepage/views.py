from django.shortcuts import render,HttpResponse
from home_app.views import c


def score(request, id):
   score = c.scorecard(id)
   info = c.matchinfo(id)
   commentary = c.commentary(id)
   send = {
            'team1':score['scorecard'][0],
            'team2':score['scorecard'][1],
            'matchinfo': info,
            'commentary':commentary,
            'bowlcard_1':score['scorecard'][0]['bowlcard']
            }

   print()
   return render(request, 'score/score.html', send)
