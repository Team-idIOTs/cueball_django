from django import forms
from django.core.validators import EMPTY_VALUES

from .models import Task, Reminders


class NewTaskForm(forms.ModelForm):

	type = forms.CharField(
		widget=forms.TextInput(
			attrs={'placeholder': 'example: Excercise, Medication, Meals'}
		),
		max_length=100,
	)	
	
	name = forms.CharField(
		widget=forms.TextInput(
			attrs={'placeholder': 'example: L-dopa, afternoon medication, stretching, boxing'}
		),
		max_length=100,
	)	
	
	message = forms.CharField(
		widget=forms.TextInput(
		attrs={'placeholder': 'Input what you would want Cueball to say to you as the reminder'}
		),
		max_length=100,
		required=False,
	)

	audio = forms.FileField(
		allow_empty_file = True,
		required = False,
		help_text='If you have a personalized voice command, upload here'
	)
	
	class Meta:
		model = Task
		fields = ['type', 'name', 'message', 'audio']

class NewReminderForm(forms.ModelForm):
	
	day = forms.CharField(
		widget=forms.TextInput(
			attrs={'placeholder': 'Days of the Week'}
		),
		max_length=100,
	)	
	
	start_time = forms.TimeField(
		widget=forms.TextInput(
		attrs={'placeholder': 'When do you want to start the reminders'}
		),
	)
	
	end_time = forms.TimeField(
		widget=forms.TextInput(
		attrs={'placeholder': 'When do you want to end the reminders'}
		),
	)

	interval_hour = forms.IntegerField(
		widget=forms.NumberInput(
		attrs={'placeholder': 'How long for this reminders'}
		),
	)

	interval_min = forms.IntegerField(
		widget=forms.NumberInput(
		attrs={'placeholder': 'How long for this reminders'}
		),
	)

	class Meta:
		model = Task
		fields = ['day', 'start_time', 'end_time']