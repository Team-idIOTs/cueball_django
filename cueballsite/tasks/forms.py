from django import forms

from .models import Task, Reminder

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
	
	day = forms.MultipleChoiceField(
		widget=forms.CheckboxSelectMultiple,
		choices = DAY_OF_WEEK,
	)	

	interval_hour = forms.IntegerField(
		widget=forms.NumberInput(
		attrs={'placeholder': 'How many hours for this reminder'}
		),
	)

	interval_min = forms.IntegerField(
		widget=forms.NumberInput(
		attrs={'placeholder': 'How many minutes for this reminder'}
		),
	)

	class Meta:
		model = Reminder
		fields = ['day', 'interval_hour', 'interval_min']