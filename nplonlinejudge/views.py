from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template
from datetime import datetime, timedelta
from programmers.models import Profile
import pytz


def home(request):
    print('THE REQUEST PATH IS:{}'.format(request.path))
    context = {'title': datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
    return render(request, 'index.html', context=context)


def about(request):
    data = dict()
    return render(request, 'about.html', {'data': data})


def leaderboard(request):
    leaderdata = Profile.objects.all().order_by('-score')
    for idx, leader in enumerate(leaderdata):
        leader.serial = idx + 1
        leader.username = leader.user.username
    if request.user.is_authenticated:
        me = leaderdata.filter(user_id=request.user.id)
        if me.exists():
            me = me[0]
            me.username = 'You'
            for idx, l in enumerate(leaderdata):
                if l.user_id == request.user.id:
                    me.serial = idx + 1
                    break
        else:
            me = dict()
    else:
        me = dict()
    return render(request, 'leaderboard.html', {'leaderboard': leaderdata, 'me': me})
