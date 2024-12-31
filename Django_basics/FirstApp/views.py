from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.
def index(request):
    return HttpResponse('<h1>Hi,Welcome to Our Django Series Page</h1>')

def second(request):
    name = 'Saugat'
    age = 19
    #always use dict 
    dict = {'name':name,'Age':age}
    return render(request,'index.html',context=dict)

def Time(request):
    date = datetime.datetime.now() #module.object.method()
    mes = 'Hello Guest !!!'
    hour = date.strftime('%H')
    if int(hour) < 12:
        mes += ' Good Morning'
    elif int(hour) < 20:
        mes += ' Good Evening'
    else:
        mes += ' Good night'
    
    dict = {'insert_time':date,'insert_mes':mes}

    return render(request,'time.html',context=dict)
