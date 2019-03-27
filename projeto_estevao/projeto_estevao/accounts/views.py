from django.shortcuts import get_object_or_404
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required, permission_required
from .forms import *
from .models import User
from django.db.models import Q
from django.db import IntegrityError, transaction
from django.urls import reverse, reverse_lazy
from dal import autocomplete
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.decorators import user_passes_test


# LISTAR USUÁRIOS
@method_decorator(login_required, name='dispatch')
class UserList(ListView):
	model = User
	template_name = 'accounts/list.html'
	http_method_names = ['get']
	context_object_name = 'object_list2'
	# paginate_by = 15

	def get_queryset(self):
		self.queryset = super(UserList, self).get_queryset()
		self.queryset = User.objects.all()
		if self.request.GET.get('search_box', False) :
			self.queryset = self.queryset.filter(Q(name__icontains = self.request.GET['search_box']) | Q(username__icontains = self.request.GET['search_box']) | Q(username__icontains = self.request.GET['search_box']))

		return self.queryset

	def get_context_data(self, **kwargs):
		_super = super(UserList, self)
		context = _super.get_context_data(**kwargs)


		context.update({
			'object_list': User.objects.all(),
			})
		return context


# DETALHAR USUÁRIO
@method_decorator(login_required, name='dispatch')
class UserDetail(UpdateView):
	model = User
	template_name = 'accounts/details.html'
	form_class = UserUpdateForm


# CRIAR USUÁRIO
@method_decorator(login_required, name='dispatch')
class UserCreate(CreateView):
	model = User
	template_name = 'accounts/add.html'
	form_class = UserForm

	def get(self, request, *args, **kwargs):
		self.object = None
		form = self.form_class
		return self.render_to_response(self.get_context_data(form=form))

	def post(self, request, *args, **kwargs):
		self.object = None
		form = self.form_class(self.request.POST, self.request.FILES)
		if form.is_valid():
			return self.form_valid(form)
		else:
			return self.form_invalid(form)

	def form_valid(self, form):

		try:
			with transaction.atomic():
				
				user = form.save()				
				messages.success(
					self.request, 'Usuário cadastrado com sucesso.')

		except IntegrityError: #If the transaction failed
			messages.error(
				self.request, 'Ocorreu um erro ao salvar o Usuário.')

		return HttpResponseRedirect(self.get_success_url())

	def form_invalid(self, form):
		return self.render_to_response(self.get_context_data(form=form))

	def get_success_url(self):
		return reverse('accounts:user_list')


# ATUALIZAR USUÁRIO
@method_decorator(login_required, name='dispatch')
class UserUpdate(UpdateView):
	model = User
	template_name = 'accounts/add.html'
	form_class = UserUpdateForm


	def get_queryset(self):
		queryset = User.objects.all()
		return queryset

	def get(self, request, *args, **kwargs):
	    self.object = self.get_object()	    
	    form = self.form_class(instance=self.object)
	    return self.render_to_response(self.get_context_data(form=form))

	def post(self, request, *args, **kwargs):
		self.object = self.get_object()

		# Deletar o avatar antigo caso o campo upload files esteja preenchido
		if self.object.avatar and self.request.FILES.get('avatar', False):
			self.object.avatar.delete()

		form = self.form_class(
			self.request.POST, self.request.FILES, instance=self.object)

		if form.is_valid():
			return self.form_valid(form)
		else:
			return self.form_invalid(form)

	def form_valid(self, form):

		try:
			with transaction.atomic():
				user = form.save()
				messages.success(
					self.request, 'Usuário atualizado com sucesso.')

		except IntegrityError: #If the transaction failed
			messages.error(
				self.request, 'Ocorreu um erro ao atualizar o cadastro do Usuário.')

		return HttpResponseRedirect(self.get_success_url())

	def form_invalid(self, form):
		return self.render_to_response(self.get_context_data(form=form))

	def get_success_url(self):
		return reverse('accounts:user_list')	


# DELETAR USUÁRIO
@login_required
def user_delete(request, pk):
	user = get_object_or_404(User, pk=pk)
	user.delete()
	return JsonResponse({'msg': "Usuário excluido com sucesso!", 'code': "200"})

