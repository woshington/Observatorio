from django.views.generic import TemplateView
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from observatorio.projeto.models import *

class Dashboard(TemplateView):
	template_name = 'dashboard/dashboard.html'

	def get_context_data(self, **kwargs):
		_super = super(Dashboard, self)
		context = _super.get_context_data(**kwargs)
		projeto = Projeto.objects.all()
		concluido = Projeto.objects.filter(status='1')
		em_andamento = Projeto.objects.filter(status='2')
		atrasado = Projeto.objects.filter(status='3')

		orcamento_pre = Projeto.objects.all().order_by('-orcamento_previsto')[:5]		
		orcamento_exe = Projeto.objects.all().order_by('-orcamento_executado')[:5]

		
		por_concluido = (concluido.count() * 100) / projeto.count()
		por_em_andamento = (em_andamento.count() * 100) / projeto.count()
		por_atrasado = (atrasado.count() * 100) / projeto.count()

		context.update({
			'projeto': projeto,
			'concluido': concluido,
			'em_andamento': em_andamento,
			'atrasado': atrasado,
			'por_concluido': por_concluido,
			'por_em_andamento': por_em_andamento,
			'por_atrasado': por_atrasado,
			'orcamento_pre': orcamento_pre,
			'orcamento_exe': orcamento_exe,
			})
		return context