from .models import *
from django.forms.utils import ErrorList
from django import forms
from dal import autocomplete
from datetime import datetime


class FaseForm(forms.ModelForm):
	
	class Meta:
		model = Fase
		fields = ['nome', 'descricao']


class CicloVidaForm(forms.ModelForm):
	# fase = forms.ModelMultipleChoiceField(
	# 	queryset=Fase.objects.all(),
	# 	label="Fases",
	# 	widget=autocomplete.ModelSelect2Multiple(url='projeto:fase_autocomplete'))
	class Meta:
		model = CicloVida
		fields = ['nome', 'fase']
		# widgets = {
		# 		'fase': autocomplete.ModelSelect2Multiple(url='projeto:fase_autocomplete')
		# }


class InstituicaoForm(forms.ModelForm):
	
	class Meta:
		model = Instituicao
		fields = ['nome', 'cidade', 'estado']