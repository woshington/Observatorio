from django.urls import path
from django.contrib.auth.decorators import permission_required
from .views import *

app_name = 'projeto'

urlpatterns = [
	
	# FASE
	path('ciclo-de-vida/fase/listar/', (FaseListar.as_view()), name='fase_listar'),
	path('ciclo-de-vida/fase/add/', (FaseCriar.as_view()), name='fase_add'),
	path('ciclo-de-vida/fase/editar/<int:pk>/', (FaseAtualizar.as_view()), name='fase_editar'),
	path('ciclo-de-vida/fase/<int:pk>/deletar/', (fase_deletar), name='fase_deletar'),
	path('ciclo-de-vida/fase/detalhar/<int:pk>/', (FaseDetalhar.as_view()), name='fase_detalhar'),
	path('ciclo-de-vida/fase/fase-autocomplete', (FaseAutocomplete.as_view()), name='fase_autocomplete'),

	# CICLO DE VIDA	
	path('ciclo-de-vida/listar/', (CicloVidaListar.as_view()), name='ciclo_vida_listar'),
	path('ciclo-de-vida/add/', (CicloVidaCriar.as_view()), name='ciclo_vida_add'),
	path('ciclo-de-vida/editar/<int:pk>/', (CicloVidaAtualizar.as_view()), name='ciclo_vida_editar'),
	path('ciclo-de-vida/<int:pk>/deletar/', (ciclo_vida_deletar), name='ciclo_vida_deletar'),
	path('ciclo-de-vida/detalhar/<int:pk>/', (CicloVidaDetalhar.as_view()), name='ciclo_vida_detalhar'),
	path('ciclo-de-vida/ciclo-de-vida-autocomplete', (CicloVidaAutocomplete.as_view()), name='ciclo_vida_autocomplete'),
    
    # INSTITUICAO
	path('instituicao/listar/', (InstituicaoListar.as_view()), name='instituicao_listar'),
	path('instituicao/add/', (InstituicaoCriar.as_view()), name='instituicao_add'),
	path('instituicao/editar/<int:pk>/', (InstituicaoAtualizar.as_view()), name='instituicao_editar'),
	path('instituicao/<int:pk>/deletar/', (instituicao_deletar), name='instituicao_deletar'),
	path('instituicao/detalhar/<int:pk>/', (InstituicaoDetalhar.as_view()), name='instituicao_detalhar'),
	path('instituicao/instituicao-autocomplete', (InstituicaoAutocomplete.as_view()), name='instituicao_autocomplete'),
	
	# MEMBRO EQUIPE
	path('membro-equipe/listar/', (MembroEquipeListar.as_view()), name='membro_equipe_listar'),
	path('membro-equipe/add/', (MembroEquipeCriar.as_view()), name='membro_equipe_add'),
	path('membro-equipe/editar/<int:pk>/', (MembroEquipeAtualizar.as_view()), name='membro_equipe_editar'),
	path('membro-equipe/<int:pk>/deletar/', (membro_equipe_deletar), name='membro_equipe_deletar'),
	path('membro-equipe/detalhar/<int:pk>/', (MembroEquipeDetalhar.as_view()), name='membro_equipe_detalhar'),
	path('membro-equipe/membro-equipe-autocomplete', (MembroEquipeAutocomplete.as_view()), name='membro_equipe_autocomplete'),    

	# PROJETO
	path('listar/', (ProjetoListar.as_view()), name='projeto_listar'),
	path('add/', (ProjetoCriar.as_view()), name='projeto_add'),
	path('editar/<int:pk>/', (ProjetoAtualizar.as_view()), name='projeto_editar'),
	path('<int:pk>/deletar/', (projeto_deletar), name='projeto_deletar'),
	path('detalhar/<int:pk>/', (ProjetoDetalhar.as_view()), name='projeto_detalhar'),
	path('projeto-autocomplete', (ProjetoAutocomplete.as_view()), name='projeto_autocomplete'),    
		
]