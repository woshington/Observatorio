from .models import *
from django.forms.utils import ErrorList
from django import forms
from dal import autocomplete
from datetime import datetime
from django.forms import inlineformset_factory




# class CicloVidaForm(forms.ModelForm):

# 	class Meta:
# 		model = CicloVida
# 		fields = ['nome_ciclo', 'fase']


class InstituicaoForm(forms.ModelForm):
	
	class Meta:
		model = Instituicao
		fields = ['nome_instituicao', 'cidade', 'estado']


class ProjetoUpdateForm(forms.ModelForm):
	
	class Meta:
		model = Projeto
		fields = ['nome', 'descricao', 'escopo', 'empresa_cliente', 'status', 'lider_projeto', 'orcamento_previsto', 'orcamento_executado', 'data_inicio', 'data_fim', 'plano_comunicacao', 'cronograma', 'atividades', 'produtos', 'riscos', 'ferramentas', 'processo_gerenciamento']


class ProjetoForm(forms.ModelForm):
	
	class Meta:
		model = Projeto
		fields = ['nome', 'descricao', 'escopo', 'empresa_cliente', 'status', 'lider_projeto', 'orcamento_previsto', 'orcamento_executado', 'data_inicio', 'data_fim', 'plano_comunicacao', 'cronograma', 'atividades', 'produtos', 'riscos', 'ferramentas', 'processo_gerenciamento']


class MembroForm(forms.ModelForm):
	
	class Meta:
		model = Membro

		fields = ('nome_membro', 'funcao')

		widgets = {
			'nome_membro': forms.TextInput(attrs={'class': 'formset-field'}),
			'funcao': forms.TextInput(attrs={'class': 'formset-field', 'style': 'width: 128px;'})
		}


class FaseForm(forms.ModelForm):
	
	class Meta:
		model = Fase
		fields = ['nome_fase', 'descricao']

		widgets = {
			'nome_fase': forms.TextInput(attrs={'class': 'formset-field'}),
			'descricao': forms.Textarea(attrs={'class': 'formset-field'})
		}
