from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .forms import SignUpForm

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
    return render(request, 'login.html', context)
	
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
