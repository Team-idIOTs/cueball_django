from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.http import HttpResponse
from django.template import loader
from django.core.files.storage import FileSystemStorage
from .models import Task

def home(request):
    title = "home"
    context = {'title': title}
    return render(request, 'home.html', context)
    
def tasks(request):
	title = "tasks"
	context = {'title': title}
	tasks = Task.objects.all()
	return render(request, 'tasks.html', {'tasks': tasks}, context)

def task_topic(request, pk):
	task = get_object_or_404(Task, pk=pk)
	return render(request, 'topics.html', {'task': task})
	    
def monitor(request):
    title = "monitor"
    context = {'title': title}
    return render(request, 'monitor.html', context)
    
def settings(request):
    title = "settings"
    context = {'title': title}
    return render(request, 'settings.html', context)
	
def add_task(request):
	title = "add_task"
	context = {'title': title}
	if request.method == 'POST':
		uploaded_file = request.FILES['document']
		fs = FileSystemStorage()
		filename = fs.save(uploaded_file.name, uploaded_file)
	return render(request, 'addtask.html', context)