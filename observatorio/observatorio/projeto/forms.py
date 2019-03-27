from .models import *
from django.forms.utils import ErrorList
from django import forms
from dal import autocomplete
from datetime import datetime


class FaseForm(forms.ModelForm):
	# descricao = forms.TextField(widget=forms.Textarea)
	
	class Meta:
		model = Fase
		fields = ['nome', 'descricao']


# class CourseForm(forms.ModelForm):

# 	lecturer = forms.ModelMultipleChoiceField(
# 		queryset=User.objects.filter(group__name="Ministrante"),
# 		label="Ministrante",
# 		widget=autocomplete.ModelSelect2Multiple(url='accounts:lecturer_autocomplete'))

# 	monitor = forms.ModelChoiceField(
# 		queryset=User.objects.filter(group__name="Monitor"),
# 		label=("Monitor"),
# 		required = False,
# 		widget=autocomplete.ModelSelect2(url='accounts:monitor_autocomplete')
# 		)

# 	season = forms.ModelChoiceField(
# 		queryset=Season.objects.filter(),
# 		label=("Periodo"),
# 		widget=autocomplete.ModelSelect2(url='school:season_autocomplete'))

# 	location = forms.ModelChoiceField(
# 		queryset=Location.objects.filter(),
# 		label=("Localização"),
# 		widget=autocomplete.ModelSelect2(url='core:location_autocomplete'))

# 	schedule = forms.ModelMultipleChoiceField(
# 		queryset=Schedule.objects.all(),
# 		label=("Horários"),
# 		widget=autocomplete.ModelSelect2Multiple(url='timetables:schedule_autocomplete'))

# 	class Meta:
# 		model = Course
# 		fields = ['name', 'season', 'lecturer', 'monitor', 'vacancies', 'schedule', 'location']

# 	def clean(self):
# 		super(CourseForm, self).clean()
# 		schedule = self.cleaned_data.get('schedule')
# 		season = self.cleaned_data.get('season')
# 		name = self.cleaned_data.get('name')
# 		location = self.cleaned_data.get('location')
# 		vacancies = self.cleaned_data.get('vacancies')

# 		if vacancies < 1:
# 			self.add_error('vacancies', 'Não se pode utilizar valor menor que 1')

# 		for s in schedule.all():
# 			if Course.objects.filter(location=location, schedule__day = s.day).exists():
# 				self.add_error('location', 'Já existe um curso cadastrado nesse horário nessa sala' + '(' + str(s.description) + ')')
