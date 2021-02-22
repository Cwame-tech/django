from django.shortcuts import render
import datetime
from django.http import HttpResponse

# Create your views here.

def index(request):
    now = datetime.datetime.now()
    day = {"Independence": now.month == 3 and now.day == 6}
    
    return render(request, 'page/indep.html', context = day)