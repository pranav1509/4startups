from django.http import HttpResponse
from django.shortcuts import render
import datetime

def hello(request):

	return HttpResponse("Hello world")

def current_datetime(request):
    now = datetime.datetime.now()
    return render(request, 'current_date.html', {'current_date': now})

