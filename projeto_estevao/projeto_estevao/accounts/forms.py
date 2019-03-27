from .models import User
from django.forms.utils import ErrorList
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm
from django import forms
from dal import autocomplete
from pycpfcnpj import cpfcnpj
from django.forms.widgets import RadioSelect
from django.contrib.auth import get_user_model


class UserForm(UserCreationForm):

	class Meta:
		model = User
		fields = ['username', 'name', 'phone', 'email', 'avatar']

	def clean(self):
		super(UserForm, self).clean()
		name = self.cleaned_data.get('name')
		username = self.cleaned_data.get('username')
		email = self.cleaned_data.get('email')

		if name == '':
			self.add_error('name','O nome é obrigatório.')

		# Valido o email para ser obrigatório
		if email == '':
			self.add_error('email', 'O endereço de email é obrigatório.')

		if email and User.objects.filter(email=email).exists():
			self.add_error('email', 'Este endereço de email já está em uso. Por favor, use um email difrerente.')


	def __init__(self, *args, **kwargs):
		super(UserForm, self).__init__(*args, **kwargs)
		self.fields['password1'].label = "Senha"
		self.fields['password2'].label = "Repita a Senha"



class UserUpdateForm(forms.ModelForm):

	class Meta:
		model = User
		fields = ['username', 'name', 'phone', 'email', 'avatar']

	def clean(self):
		super(UserUpdateForm, self).clean()
		name = self.cleaned_data.get('name')
		username = self.cleaned_data.get('username')
		email = self.cleaned_data.get('email')

		if name == '':
			self.add_error('name','O nome é obrigatório.')


class PasswordResetForm(PasswordResetForm):
	def clean_email(self):
		amount = get_user_model()._default_manager.filter(
			email__iexact=self.cleaned_data.get('email'), is_active=True).count()
		if(amount < 1):
			raise forms.ValidationError('Lamentamos, mas não reconhecemos esse endereço de e-mail.')
		return self.cleaned_data.get('email')


