from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template
from datetime import datetime, timedelta
import pytz


def home(request):
    print('THE REQUEST PATH IS:{}'.format(request.path))
    context = {'title': datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
    return render(request, 'index.html', context=context)


def about(request):
    context = {'title': 'About Us'}
    templatepage = 'base.html'
    templatepageobj = get_template(templatepage)
    return HttpResponse(templatepageobj.render(context))
