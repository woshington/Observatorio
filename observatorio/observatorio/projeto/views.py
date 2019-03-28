from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic.edit import CreateView, DeleteView, UpdateView, FormView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .forms import *
from .models import *
from django.db.models import Q
from django.db import IntegrityError, transaction
from django.urls import reverse, reverse_lazy
from dal import autocomplete, forward
from datetime import datetime
from datetime import timedelta
from django.dispatch import receiver
from datetime import datetime
from django.contrib import messages


class FaseListar(ListView):
	model = Fase
	http_method_names = ['get']
	template_name = 'fase/listar.html'
	context_object_name = 'object_list'
	paginate_by = 20

	def get_queryset(self):
		self.queryset = super(FaseListar, self).get_queryset()
		if self.request.GET.get('search_box', False):
			self.queryset=self.queryset.filter(Q(nome__icontains=self.request.GET['search_box']))
		return self.queryset

	def get_context_data(self, **kwargs):
		_super = super(FaseListar, self)
		context = _super.get_context_data(**kwargs)
	
		context.update({
			})
		return context


class FaseCriar(CreateView):
	model = Fase
	template_name = 'fase/add.html'
	form_class = FaseForm


class FaseDetalhar(UpdateView):
	model = Fase
	template_name = 'fase/detalhar.html'
	form_class = FaseForm


class FaseAtualizar(UpdateView):
	model = Fase
	template_name = 'fase/add.html'
	form_class = FaseForm


def fase_deletar(request, pk):
	fase = get_object_or_404(Fase, pk=pk)
	fase.delete()
	return redirect('projeto:fase_listar')


class FaseAutocomplete(autocomplete.Select2QuerySetView):
	def get_queryset(self):
		qs = Fase.objects.all()

		if self.q:
			qs = qs.filter(nome__icontains=self.q)

		return qs


class CicloVidaListar(ListView):
	model = CicloVida
	http_method_names = ['get']
	template_name = 'ciclo_vida/listar.html'
	context_object_name = 'object_list'
	paginate_by = 20

	def get_queryset(self):
		self.queryset = super(CicloVidaListar, self).get_queryset()
		if self.request.GET.get('search_box', False):
			self.queryset=self.queryset.filter(Q(nome__icontains=self.request.GET['search_box']))
		return self.queryset

	def get_context_data(self, **kwargs):
		_super = super(CicloVidaListar, self)
		context = _super.get_context_data(**kwargs)
	
		context.update({
			})
		return context


class CicloVidaCriar(CreateView):
	model = CicloVida
	template_name = 'ciclo_vida/add.html'
	form_class = CicloVidaForm


class CicloVidaDetalhar(UpdateView):
	model = CicloVida
	template_name = 'ciclo_vida/detalhar.html'
	form_class = CicloVidaForm


class CicloVidaAtualizar(UpdateView):
	model = CicloVida
	template_name = 'ciclo_vida/add.html'
	form_class = CicloVidaForm


def ciclo_vida_deletar(request, pk):
	ciclo_vida = get_object_or_404(CicloVida, pk=pk)
	ciclo_vida.delete()
	return redirect('projeto:ciclo_vida_listar')


class CicloVidaAutocomplete(autocomplete.Select2QuerySetView):
	def get_queryset(self):
		qs = CicloVida.objects.all()

		if self.q:
			qs = qs.filter(nome__icontains=self.q)

		return qs


class InstituicaoListar(ListView):
	model = Instituicao
	http_method_names = ['get']
	template_name = 'instituicao/listar.html'
	context_object_name = 'object_list'
	paginate_by = 20

	def get_queryset(self):
		self.queryset = super(InstituicaoListar, self).get_queryset()
		if self.request.GET.get('search_box', False):
			self.queryset=self.queryset.filter(Q(nome__icontains=self.request.GET['search_box']))
		return self.queryset

	def get_context_data(self, **kwargs):
		_super = super(InstituicaoListar, self)
		context = _super.get_context_data(**kwargs)
	
		context.update({
			})
		return context


class InstituicaoCriar(CreateView):
	model = Instituicao
	template_name = 'instituicao/add.html'
	form_class = InstituicaoForm


class InstituicaoDetalhar(UpdateView):
	model = Instituicao
	template_name = 'instituicao/detalhar.html'
	form_class = InstituicaoForm


class InstituicaoAtualizar(UpdateView):
	model = Instituicao
	template_name = 'instituicao/add.html'
	form_class = InstituicaoForm


def instituicao_deletar(request, pk):
	instituicao = get_object_or_404(Instituicao, pk=pk)
	instituicao.delete()
	return redirect('projeto:instituicao_listar')
		