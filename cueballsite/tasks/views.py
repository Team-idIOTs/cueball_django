from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Count
from django.core.files.storage import FileSystemStorage

from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .models import Task, Reminder
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
def task_topic(request, pk):
	title = "tasks"
	task = get_object_or_404(Task, pk=pk)
	context = {'task': task, 'title':title}
	return render(request, 'topic.html', context)

@login_required
def task_reminder(request, pk, reminder_pk):
	title = "tasks"
	reminder = get_object_or_404(Reminder, task_id=pk, id=reminder_pk)
	context = {'reminder':reminder, 'title':title}
	return render(request, 'task_reminder.html', context)

@login_required
def add_task(request):
	title = 'tasks'
	if request.method == 'POST':
		form = NewTaskForm(request.POST)
		if form.is_valid():
			task = form.save(commit=False)
			task.starter = request.user
			task.save()
			reminder = Reminder.objects.create(
				task = task,
				created_by = request.user,
			)
			# data = {
				# 'type': type,
				# 'title': title,
			# }
			# print(data)
			# db.post(data)
			return redirect('task_topic', task.id)
	else:
		form = NewTaskForm()
	return render(request, 'addtask.html', {'form':form})

@login_required
def add_reminder(request, pk):
	title = 'tasks'
	reminder = get_object_or_404(Reminder, task_id=pk)
	if request.method == 'POST':
		form = NewReminderForm(request.POST)
		if form.is_valid():
			reminder = form.save(commit=False)
			reminder.task = task
			reminder.created_by = request.user
			reminder.save()
			
			return redirect('task_reminder', task_id=pk, id=reminder_pk)

	else:
		form = NewReminderForm()
	return render(request, 'addreminder.html', {'form':form})