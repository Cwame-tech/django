from django.shortcuts import render
import datetime
from django.http import HttpResponse
# Create your views here.

def index(request):
    now = datetime.datetime.now()
    context = {"Republic_day": now.month == 7 and now.day == 1}
    
    return render(request, 'Repuday/index.html', context = context)