from django import forms
from django.forms.utils import ErrorList
from dal import autocomplete, forward
from observatorio.projeto.models import *


class OrcamentoMaiorQueForm(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(OrcamentoMaiorQueForm, self).__init__(*args, **kwargs)
		self.fields['orcamento_previsto'].required = False

	class Meta:
		model = Projeto
		fields = ['orcamento_previsto']


