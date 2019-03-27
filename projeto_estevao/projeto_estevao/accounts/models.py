import re
import uuid
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractBaseUser, UserManager, PermissionsMixin
from easy_thumbnails.fields import ThumbnailerImageField
from django.core import validators
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType


class User(AbstractBaseUser, PermissionsMixin):

	username = models.CharField(
		'Usuário', max_length=100, default=uuid.uuid4, unique=True, validators=[
			validators.RegexValidator(
				re.compile('^[\w.@+-]+$'),
				'Informe um nome de usuário válido. '
				'Este valor deve conter apenas letras, números '
				'e os caracteres: @/./+/-/_ .'
				, 'invalid'
			)
		], help_text='Um nome curto que será usado para identificá-lo de forma única na plataforma'
	)

	name = models.CharField('Nome', max_length=100, blank=True)
	email = models.EmailField('E-mail', blank=True, null=True)
	is_staff = models.BooleanField('Equipe', default=False)
	is_superuser = models.BooleanField('Super Usuário', default=False)
	is_active = models.BooleanField('Ativo', default=True)
	phone = models.CharField('Telefone', max_length=16, blank=True, null=True)
	avatar = ThumbnailerImageField(
		upload_to="avatar",
		blank=True,
		resize_source=dict(size=(215, 215), crop=True)
	)
	
	objects = UserManager()

	EMAIL_FIELD = 'email'
	USERNAME_FIELD = 'username'
	REQUIRED_FIELDS = ['email']

	def __str__(self):
		return self.name or self.username

	def has_perm(self, perm, obj=None):
		"Does the user have a specific permission?"
    	# Simplest possible answer: Yes, always
		return True

	def has_module_perms(self, app_label):
		"Does the user have permissions to view the app `app_label`?"
		# Simplest possible answer: Yes, always
		return True

	def get_full_name(self):
		return str(self)

	def get_short_name(self):
		return str(self).split(" ")[0]

	def get_absolute_url(self):
		return reverse('accounts:user_list')

	""" Método deletar a imagem (avatar) quando alterada ou excluida """
	def delete(self):
		self.avatar.delete()
		return super(User, self).delete()

	class Meta:
		verbose_name = 'Usuário'
		verbose_name_plural = 'Usuários'
		ordering = ['name']
