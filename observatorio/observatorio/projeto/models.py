import re
import uuid
from django.db import models
from django.urls import reverse
from django.core import validators
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from easy_thumbnails.fields import ThumbnailerImageField
from django.core import validators


class AuditModel(models.Model):
	# Audit Fields
	created_on = models.DateTimeField('Criado em', auto_now_add=True)
	updated_on = models.DateTimeField('Autalizado em', auto_now=True)

	class Meta:
		abstract=True


class Fase(AuditModel):
	nome = models.CharField('Nome', max_length=255)
	descricao = models.TextField('Descricao')

	def __str__(self):
		return self.nome

	def get_absolute_url(self):
		return reverse('projeto:fase_listar')

	class Meta:
		verbose_name = 'Fase'
		verbose_name_plural = 'Fases'
		ordering = ['id']	


class CicloVida(AuditModel):
	nome = models.CharField('Nome', max_length=255)
	fase = models.ManyToManyField(Fase,verbose_name='Fases', blank=True)

	def __str__(self):
		return self.nome

	def get_absolute_url(self):
		return reverse('projeto:ciclo_vida_listar')

	class Meta:
		verbose_name = 'Ciclo de Vida'
		verbose_name_plural = 'Ciclos de Vida'
		ordering = ['nome']	


class Instituicao(models.Model):
	nome = models.CharField('Instituição', max_length=255, unique=True)
	cidade = models.CharField('Cidade', max_length=255, blank=True, null=True)
	estado = models.CharField('UF', max_length=2, blank=True, null=True)

	def __str__(self):
		return self.nome

	def get_absolute_url(self):
		return reverse('projeto:instituicao_listar')

	class Meta:
		verbose_name = 'Instituição'
		verbose_name_plural = 'Instituições'
		ordering = ['nome']


class MembroEquipe(models.Model):
	nome = models.CharField('Nome', max_length=255)
	funcao = models.CharField('Função', max_length=255)

	def __str__(self):
		return self.nome

	def get_absolute_url(self):
		return reverse('projeto:membro_equipe_listar')	

	class Meta:
		verbose_name = 'Membro da Equipe'
		verbose_name_plural = 'Membros da Equipe'
		ordering = ['nome']


class Projeto(models.Model):
	nome = models.CharField('Nome ou Sigla', max_length=255, unique=True)
	instituicao = models.ForeignKey(Instituicao, on_delete=models.CASCADE, default=False)
	escopo = models.TextField('Escopo')
	atividades = models.TextField('Atividades')
	membros = models.ManyToManyField(MembroEquipe,verbose_name='Membros', blank=True)
	produtos = models.TextField('Produtos e/ou serviços entregues')
	orcamento_previsto = models.FloatField('Orçamento previsto', null=True, blank=True, default=None)
	orcamento_executado = models.FloatField('Orçamento executado', null=True, blank=True, default=None)
	data_inicio = models.DateTimeField('Data do inicio')
	data_fim = models.DateTimeField('Data do fim')
	ciclo_vida = models.ForeignKey(CicloVida, verbose_name="Ciclo de Vida", on_delete=models.CASCADE, default=False)
	plano_comunicacao = models.TextField('Plano de comunicacao')
	cronograma = models.FileField('Cronograma', upload_to='cronograma/')
	riscos = models.TextField('Riscos')
	ferramentas = models.TextField('Ferramentas utilizadas para gestão do projeto')
	processo_gerenciamento = models.TextField('Processo de gerenciamento de mudanças')

	STATUS = (
        ('0', ''),
        ('1', 'Concluido'),
        ('2', 'Em andamento'),
        ('3', 'Atrasado'),
    )
	status = models.CharField(
		'Status',
		max_length=1,
		choices=STATUS,
		default='0'
	)
	 
	def __str__(self):
		return self.nome

	def get_absolute_url(self):
		return reverse('projeto:projeto_listar')

	""" Método deletar o arquivo de cronogrma quando alterado ou excluido """
	def delete(self):
		self.cronograma.delete()
		return super(Projeto, self).delete()		

	class Meta:
		verbose_name = 'Projetos'
		verbose_name_plural = 'Projetos'
		ordering = ['nome']





						