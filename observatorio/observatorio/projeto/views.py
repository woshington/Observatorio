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
	fase = get_object_or_404(Fase,pk=pk)
	fase.delete()
	return redirect('projeto:fase_listar')