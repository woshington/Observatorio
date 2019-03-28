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
	descricao = models.TextField('Descrição')
	instituicao = models.ForeignKey(Instituicao, on_delete=models.CASCADE, default=False)
	empresa_cliente = models.CharField('Empresa Cliente', max_length=255, blank=True)
	escopo = models.TextField('Escopo', blank=True)
	atividades = models.TextField('Atividades', blank=True)
	lider_projeto = models.CharField('Líder do Projeto', max_length=255, blank=True)
	membros = models.ManyToManyField(MembroEquipe,verbose_name='Membros', blank=True)
	produtos = models.TextField('Produtos e/ou serviços entregues', blank=True)
	orcamento_previsto = models.FloatField('Orçamento previsto', null=True, blank=True, default=None)
	orcamento_executado = models.FloatField('Orçamento executado', null=True, blank=True, default=None)
	data_inicio = models.DateTimeField('Data do inicio')
	data_fim = models.DateTimeField('Data do fim')
	ciclo_vida = models.ForeignKey(CicloVida, verbose_name="Ciclo de Vida", on_delete=models.CASCADE, default=False)
	plano_comunicacao = models.FileField('Plano de comunicacao', upload_to='plano_comunicacao/', blank=True)
	cronograma = models.FileField('Cronograma', upload_to='cronograma/', blank=True)
	riscos = models.TextField('Riscos', blank=True)
	ferramentas = models.TextField('Ferramentas utilizadas para gestão do projeto', blank=True)
	processo_gerenciamento = models.TextField('Processo de gerenciamento de mudanças', blank=True)

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
		default='2'
	)

	def por_concluido(self):
		concluido = Projeto.objects.filter(status='1')
		print("Eita", ((concluido.count() * 100) / self.count()))
		return "eita"

	def por_em_andamento(self):
		em_andamento = Projeto.objects.filter(status='2')
		return (em_andamento.count * 100) / self.count()

	def por_atrasado(self):
		atrasado = Projeto.objects.filter(status='2')
		return (atrasado * 100) / self.count()		
	 
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





						