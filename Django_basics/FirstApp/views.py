from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect

import datetime
from FirstApp.models import StudentInfo
from FirstApp.models import PhotoFromExternal
from FirstApp.models import form_submission as FormSubmission
#from FirstApp.forms import StudentForm
from FirstApp.forms import form_submission  
from . import forms
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

def Student(request):
    info = StudentInfo.objects.all()
    logo = PhotoFromExternal.objects.all()
    dict = {'info':info,'logo':logo}
    return render(request,'flexcard.html',context=dict)


def Student_Record(request):
    if request.method == 'POST':
        form = form_submission(request.POST)
        if form.is_valid():
            name = form.cleaned_data['user_name']
            password = form.cleaned_data['user_password']
            print(f"Name:{name} \nPassword:{password}")
            FormSubmission.objects.create(user_name=name, user_password=password)
            
    else:
        form = form_submission()

    return render(request, 'student.html', {'form': form})




