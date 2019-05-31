from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Count
from django.contrib.auth.models import User

from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from .models import Task, Reminders
from .forms import NewTaskForm, NewReminderForm


def home(request):
    title = "home"
    context = {'title': title}
    return render(request, 'home.html', context)
 
@login_required
def tasks(request):
	title = "tasks"
	tasks = Task.objects.all()
	return render(request, 'tasks.html', {'tasks':tasks, 'title':title})

@login_required
def task_topic(request, pk):
	title = "tasks"
	task = get_object_or_404(Task, pk=pk)
	return render(request, 'task_reminder.html', {'task': task, 'title':title})

@login_required
def monitor(request):
	title = "monitor"
	context = {'title': title}
	return render(request, 'monitor.html', context)

@login_required
def settings(request):
    title = "settings"
    context = {'title': title}
    return render(request, 'settings.html', context)
	
@login_required
def add_task(request):
	title = 'tasks'
	if request.method == 'POST':
		form = NewTaskForm(request.POST)
		if form.is_valid():
			task = form.save(commit=False)
			task.starter = request.user
			task.save()
			reminder = Reminders.objects.create(
				task = task,
				created_by = request.user,
			)
			return redirect('tasks')
	else:
		form = NewTaskForm()
	return render(request, 'addtask.html', {'form':form})

@login_required
def add_reminder(request, pk, task_pk):
	title = 'tasks'
	reminder = get_object_or_404(Reminders, task_pk=pk, pk=reminder_pk)
	if request.method == 'POST':
		form = NewReminderForm(request.POST)
		if form.is_valid():
			reminder = form.save(commit=False)
			reminer.task = task
			task.starter = request.user
			reminder.save()
			Reminders.objects.create(
				day='day',
			start_time='start_time',
				end_time='end_time'
				#interval_hour='interval_hour'
				#interval_min='interval_min'
				#created_by = request.user
			)	
			return redirect('tasks', pk=pk, task_pk = task_pk)
	else:
		form = NewReimderForm()
	return render(request, 'addreminder.html', {'form':form})