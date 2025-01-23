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
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login
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


# def signin_page(request):
#     form_signin = form_submission()
#     if request.method == "POST":
#         form_signin = form_submission(request.POST)
#         if form_signin.is_valid():
#             name = form_signin.cleaned_data['user_name']
#             password = form_signin.cleaned_data['user_password']
#             print(f"Name:{name} \nPassword:{password}")
#             data_of_signup = FormSubmission.objects.all()
#             print(type(data_of_signup))
#             # for user_name,user_password in data_of_signup:
#             #     if(name == data_of_signup.user_name & password == data_of_signup.user_password):
#             #         print('success')
#         else:
#             form_signin = form_submission()
    
#     return render(request,'signin.html',{'form':form_signin})



def sign_in(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully logged in")
            return redirect('home')  # Redirect to home page or any other page
        else:
            messages.error(request, "Invalid credentials")
            return redirect('sign_in')
    
    return render(request, 'signin.html')

def register(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password = request.POST.get('password')
        username = request.POST.get('username')

        # Check if the username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username is already in use.")
            return redirect('register')

        # Create the user with the password set directly
        user = User.objects.create_user(
            username=username,
            first_name=first_name,
            last_name=last_name,
            password=password  # Set the password here
        )

        messages.success(request, "Account created successfully!")
        return redirect('sign_in')

    return render(request, 'register.html')

    
