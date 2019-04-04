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
from django.forms.formsets import formset_factory
from django.forms import modelformset_factory

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
	return JsonResponse({'msg': "Administrador excluido com sucesso!", 'code': "1"})


class InstituicaoAutocomplete(autocomplete.Select2QuerySetView):
	def get_queryset(self):
		qs = Instituicao.objects.all()

		if self.q:
			qs = qs.filter(nome__icontains=self.q)

		return qs


class MembroListar(ListView):
	model = Membro
	http_method_names = ['get']
	template_name = 'membro/listar.html'
	context_object_name = 'object_list'
	paginate_by = 20

	def get_queryset(self):
		self.queryset = super(MembroListar, self).get_queryset()
		if self.request.GET.get('search_box', False):
			self.queryset=self.queryset.filter(Q(nome__icontains=self.request.GET['search_box']))
		return self.queryset

	def get_context_data(self, **kwargs):
		_super = super(MembroListar, self)
		context = _super.get_context_data(**kwargs)
	
		context.update({
			})
		return context


class MembroCriar(CreateView):
	model = Membro
	template_name = 'membro/add.html'
	form_class = MembroForm


class MembroDetalhar(UpdateView):
	model = Membro
	template_name = 'membro/detalhar.html'
	form_class = MembroForm


class MembroAtualizar(UpdateView):
	model = Membro
	template_name = 'membro/add.html'
	form_class = MembroForm


def membro_deletar(request, pk):
	membro = get_object_or_404(Membro, pk=pk)
	membro.delete()
	return JsonResponse({'msg': "Administrador excluido com sucesso!", 'code': "1"})


class MembroAutocomplete(autocomplete.Select2QuerySetView):
	def get_queryset(self):
		qs = Membro.objects.all()

		if self.q:
			qs = qs.filter(nome__icontains=self.q)

		return qs


class ProjetoListar(ListView):
	model = Projeto
	http_method_names = ['get']
	template_name = 'projeto/listar.html'
	context_object_name = 'object_list'
	paginate_by = 20

	def get_queryset(self):
		self.queryset = super(ProjetoListar, self).get_queryset()
		if self.request.GET.get('search_box', False):
			self.queryset=self.queryset.filter(Q(nome__icontains=self.request.GET['search_box']))
		return self.queryset

	def get_context_data(self, **kwargs):
		_super = super(ProjetoListar, self)
		context = _super.get_context_data(**kwargs)
	
		context.update({
			})
		return context


class ProjetoCriar(CreateView):
	template_name = 'projeto/add.html'
	models = Projeto
	form_class = ProjetoForm
	second_form_class = InstituicaoForm
	third_form_class = MembroForm


	def get(self, request, *args, **kwargs):
		self.object = None
		form = self.form_class
		instituicao_form = self.second_form_class
		membro_form = self.third_form_class

		MembroFormset = modelformset_factory(Membro, form=MembroForm)
		formset = MembroFormset(request.POST or None, queryset= Membro.objects.none(), prefix='membro')

		# FaseFormset = modelformset_factory(Fase, form=FaseForm)		
		# fase_formset = FaseFormset(request.POST or None, queryset= Fase.objects.none(), prefix='fase')

		return self.render_to_response(
			self.get_context_data(
				form=form,
				instituicao_form=instituicao_form,
				membro_form=membro_form,
				formset= formset,
			)
		)

	def post(self, request, *args, **kwargs):
		self.object = None
		form = self.form_class(self.request.POST, self.request.FILES)
		instituicao_form = self.second_form_class(self.request.POST)
		
		MembroFormset = modelformset_factory(Membro, form=MembroForm)
		formset = MembroFormset(request.POST or None, queryset= Membro.objects.none(), prefix='membro')

		# FaseFormset = modelformset_factory(Fase, form=FaseForm)		
		# fase_formset = FaseFormset(request.POST or None, queryset= Fase.objects.none(), prefix='fase')

		if form.is_valid() and instituicao_form.is_valid() and formset.is_valid():
			return self.form_valid(form, instituicao_form, formset)
		else:
			return self.form_invalid(form, instituicao_form, formset)

	def form_valid(self, form, instituicao_form, formset):

		try:
			with transaction.atomic():

				instituicao = instituicao_form.save()				
				projeto = form.save(commit=False)
				projeto.instituicao = instituicao

				projeto.save()

				# Membros
				for item in formset:
					data = item.save(commit=False)
					data.projeto = projeto
					data.save()



		except IntegrityError: #If the transaction failed
			messages.error(
				self.request, 'Ocorreu um erro ao salvar o projeto.')

		# return HttpResponseRedirect(self.get_success_url())
		return redirect('projeto:projeto_add_fase', pk=projeto.id)

	def form_invalid(self, form, instituicao_form, formset):
		return self.render_to_response(
			self.get_context_data(
					form=form,
					instituicao_form=instituicao_form,
					formset=formset,

				)
			)

	def get_success_url(self):
		return reverse('projeto:projeto_listar')



class ProjetoCriarFases(CreateView):
	template_name = 'projeto/add_fase.html'
	models = Fase
	form_class = FaseForm

	def get(self, request, *args, **kwargs):
		self.object = None
		
		FaseFormset = modelformset_factory(Fase, form=FaseForm)		
		formset = FaseFormset(request.POST or None, queryset= Fase.objects.none(), prefix='fase')

		return self.render_to_response(
			self.get_context_data(
				formset= formset
			)
		)

	def post(self, request, *args, **kwargs):
		self.object = None
	
		FaseFormset = modelformset_factory(Fase, form=FaseForm)		
		formset = FaseFormset(request.POST or None, queryset= Fase.objects.none(), prefix='fase')

		if formset.is_valid():
			return self.form_valid(formset)
		else:
			return self.form_invalid(formset)

	def form_valid(self, formset, **kwargs):

		try:
			with transaction.atomic():
				
				projeto = get_object_or_404(Projeto, pk=self.kwargs['pk'])
				
				# Fases
				for item in formset:
					data = item.save(commit=False)
					data.projeto = projeto
					data.save()



		except IntegrityError: #If the transaction failed
			messages.error(
				self.request, 'Ocorreu um erro ao salvar o projeto.')

		return HttpResponseRedirect(self.get_success_url())

	def form_invalid(self, form, instituicao_form, formset):
		return self.render_to_response(
			self.get_context_data(
					form=form,
					instituicao_form=instituicao_form,
					formset=formset,

				)
			)

	def get_success_url(self):
		return reverse('projeto:projeto_listar')



class ProjetoDetalhar(DetailView):
	model = Projeto
	template_name = 'projeto/detalhar.html'

	def get_context_data(self, **kwargs):
		_super = super(ProjetoDetalhar, self)
		context = _super.get_context_data(**kwargs)
		projeto = get_object_or_404(Projeto, pk=self.kwargs['pk'])
	
		context.update({
			'membros': Membro.objects.filter(projeto = projeto),
			'fases': Fase.objects.filter(projeto = projeto)

			})
		return context


class ProjetoAtualizar(UpdateView):
	model = Projeto
	template_name = 'projeto/add.html'
	form_class = ProjetoUpdateForm


def projeto_deletar(request, pk):
	projeto = get_object_or_404(Projeto, pk=pk)
	projeto.delete()
	return JsonResponse({'msg': "Administrador excluido com sucesso!", 'code': "1"})


class ProjetoAutocomplete(autocomplete.Select2QuerySetView):
	def get_queryset(self):
		qs = Projeto.objects.all()

		if self.q:
			qs = qs.filter(nome__icontains=self.q)

		return qs


def step1(request):    
	form = ProjetoForm(request.POST or None)
	if request.method == 'POST':
		if form.is_valid():
			projeto = form.save()
			request.session['pk'] = projeto.id
			return HttpResponseRedirect(reverse('projeto_add_step2'))
	return render(request, 'projeto/step1.html', {'form': form})


def step2(request):
	form = InstituicaoForm(request.POST or None)
	if request.method == 'POST':
		if form.is_valid():
			instituicao = form.save()
			projeto = get_object_or_404(Projeto, pk=request.session['pk'])
			projeto.instituicao=instituicao
			projeto.save()
			return HttpResponseRedirect(reverse('projeto:projeto_listar'))
	return render(request, 'projeto/step2.html', {'form': form})
