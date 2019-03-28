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


class MembroEquipeForm(forms.ModelForm):
	
	class Meta:
		model = MembroEquipe
		fields = ['nome', 'funcao']


class ProjetoForm(forms.ModelForm):
	
	class Meta:
		model = Projeto
		fields = ['nome', 'descricao','instituicao', 'empresa_cliente', 'status','escopo', 'atividades', 'lider_projeto','membros', 'produtos', 'orcamento_previsto', 'orcamento_executado', 'data_inicio', 'data_fim', 'ciclo_vida', 'plano_comunicacao', 'cronograma', 'riscos', 'ferramentas', 'processo_gerenciamento']		