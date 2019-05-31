from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Task(models.Model):
	type = models.CharField(max_length=100)
	name = models.CharField(max_length=30, unique=True)
	audio = models.FileField(upload_to='media/', null=True, blank=True)
	message = models.TextField(max_length=100)
	starter = models.ForeignKey(User, related_name='task', on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(null=True)
	
	def __str__(self):
		return self.name
		
class Reminders(models.Model):
	MON = 'M'
	TUE = 'T'
	WED = 'W'
	THU = 'R'
	FRI = 'F'
	SAT = 'S'
	SUN = 'U'
	DAY_OF_WEEK = [
		(MON, 'Monday'),
		(TUE, 'Tuesday'),
		(WED, 'Wednesday'),
		(THU, 'Thursday'),
		(FRI, 'Friday'),
		(SAT, 'Saturday'),
		(SUN, 'Sunday'),
		]
	task = models.ForeignKey(Task, related_name='reminders', on_delete=models.CASCADE)
	day = models.CharField(max_length=1, choices=DAY_OF_WEEK)
	start_time = models.TimeField(null=True)
	end_time = models.TimeField(null=True)
	interval_hour = models.IntegerField(null=True)
	interval_min = models.IntegerField(null=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(null=True)
	created_by = models.ForeignKey(User, related_name='reminders', on_delete=models.CASCADE)
	updated_by = models.ForeignKey(User, null=True, related_name='+', on_delete=models.CASCADE)