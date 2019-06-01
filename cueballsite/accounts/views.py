from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .forms import SignUpForm

import pyrebase

config = {
	'apiKey': "AIzaSyDnRM1b-dOfkqmaQ94BJyG-0lCo114LPmA",
	'authDomain': "reminders-56e2c.firebaseapp.com",
	'databaseURL': "https://reminders-56e2c.firebaseio.com",
	'projectId': "reminders-56e2c",
	'storageBucket': "reminders-56e2c.appspot.com",
	'messagingSenderId': "708737581745",
  };
 
firebase = pyrebase.initialize_app(config);
auth = firebase.auth()

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('tasks')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})
	
def login(request):
	title = "login"
	context = {'title': title}
	try:
		user = authe.sign_in_with_email_and_password(email,password)
	except:
		error="Unable to access account, try again"
		return render(request,"login.html",{"messg":error})
	print(user['localid'])
	session_id=user['localid']
	request.session['uid']=str(session_id)
	return render(request, 'login.html', context)

def logout(request):
    auth.logout(request)
    return render(request,'home.html')
	
def password_reset(request):
    title = "password_reset"
    context = {'title': title}
    return render(request, 'password_reset.html', context)
		
def password_reset_done(request):
    title = "password_reset_done"
    context = {'title': title}
    return render(request, 'password_reset_done.html', context)
	
def password_reset_done(request):
    title = "password_reset_done"
    context = {'title': title}
    return render(request, 'password_reset_done.html', context)
	
def password_reset_complete(request):
    title = "password_reset_complete"
    context = {'title': title}
    return render(request, 'password_reset_complete.html', context)
	
def password_change(request):
    title = "password_change"
    context = {'title': title}
    return render(request, 'password_change.html', context)

def password_change_done(request):
    title = "password_change_done"
    context = {'title': title}
    return render(request, 'password_change_done.html', context)	
