from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic.edit import CreateView, DeleteView, UpdateView, FormView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required, permission_required
from .forms import *
from observatorio.projeto.models import *
from django.db.models import Q
from django.db import IntegrityError, transaction
from django.urls import reverse, reverse_lazy
from dal import autocomplete, forward
from datetime import datetime
from datetime import timedelta
from django.dispatch import receiver
from datetime import datetime
from django.contrib import messages


class OrcamentoMaiorQue(FormView,ListView):
	model = Projeto
	template_name = 'consultas/orcamento_maior_que.html'
	form_class = OrcamentoMaiorQueForm

	def get_context_data(self, **kwargs):
		context = super(OrcamentoMaiorQue, self).get_context_data(**kwargs)
		
		if self.request.GET.get('orcamento_previsto'):

			projeto = get_object_or_404(Projeto,pk=self.request.GET.get('orcamento_previsto'))
			
			consulta_lista = Projeto.objects.filter(orcamento_previsto < projeto.orcamento_previsto)
			
			context.update({
				'consulta_lista': consulta_lista,
				})
		return context



# class ReportStudentCourses(FormView,ListView):
# 	model = User
# 	template_name = 'report/report_student_courses.html'
# 	form_class = ReportStudentCoursesForm

# 	def get_context_data(self, **kwargs):
# 		context = super(ReportStudentCourses, self).get_context_data(**kwargs)
# 		# Se existir a variavel name no get
# 		if self.request.GET.get('name'):
# 			# Recupera o estudante
# 			print('papapapa: ',self.request.GET.get('name'))

# 			student = get_object_or_404(User,pk=self.request.GET.get('name'))

# 			courses = Registration.objects.filter(student = student)
# 			context.update({
# 				'student': student,
# 				'courses': courses,
# 				})
# 		return context


# @method_decorator(login_required, name='dispatch')
# class ReportCourse(FormView,ListView):
# 	model = Registration
# 	template_name = 'report/report_course.html'
# 	form_class = ReporttRegistrationForm

# 	def get_context_data(self, **kwargs):
# 		context = super(ReportCourse, self).get_context_data(**kwargs)
# 		# Se existir a variavel registration no get
# 		if self.request.GET.get('registration'):
# 			# Recupera a matricula
# 			registration = get_object_or_404(Registration,pk=self.request.GET.get('registration'))
# 			print("Registration", registration)
# 			context.update({
# 				'registration': registration,
# 				})
# 		return context


# # LISTA TODOS OS ESTUDANTES
# @method_decorator(login_required, name='dispatch')
# class ReportAllStudents(ListView):
# 	model = User
# 	template_name = 'report/list_all_students.html'
# 	http_method_names = ['get']
# 	context_object_name = 'object_list'

# 	def get_queryset(self):
# 		return User.objects.filter(group__name = "Estudante")


# # LISTA TODOS OS MONITORES
# @method_decorator(login_required, name='dispatch')
# class ReportAllMonitors(ListView):
# 	model = User
# 	template_name = 'report/list_all_monitors.html'
# 	http_method_names = ['get']
# 	context_object_name = 'object_list'
	
# 	def get_queryset(self):
# 		return User.objects.filter(group__name = "Monitor")


# # LISTA TODOS OS MINISTRANTES
# @method_decorator(login_required, name='dispatch')
# class ReportAllLecturers(ListView):
# 	model = User
# 	template_name = 'report/list_all_lecturers.html'
# 	http_method_names = ['get']
# 	context_object_name = 'object_list'

# 	def get_queryset(self):
# 		return User.objects.filter(group__name = "Ministrante")


