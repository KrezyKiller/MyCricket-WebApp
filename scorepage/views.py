from django.shortcuts import render,HttpResponse
from home_app.views import c


def score(request, id):
   score = c.scorecard(id)
   info = c.matchinfo(id)
   commentary = c.commentary(id)
   print(commentary)
   send = {
                 'matchinfo': info,
                 'commentary':commentary['commentary'],
                 }
   if info['mchstate'] == 'mom' or 'inprogress' or 'innings break':
      try:
          send['status'] = 'Ok'
          send['team1'] = score['scorecard'][0]
          send['bowlcard_1'] = score['scorecard'][0]['bowlcard'],
          send['team2'] = score['scorecard'][1]
          send['bowlcard_2'] = score['scorecard'][1]['bowlcard']
      except:
          send['team2'] = ['None']
          send['status'] = 'Preview'
   return render(request, 'score/score.html',send)
