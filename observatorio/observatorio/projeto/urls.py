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
	# path('ciclo-de-vida/fase/projeto-autocomplete', ion=True)(ProjetoAutocomplete.as_view()), name='fase_autocomplete'),

	
    
	# SEASON
	# path('listar/', (ProjetoList.as_view()), name='projeto_listar'),
	# path('add/', (ProjetoCreate.as_view()), name='projeto_add'),
	# path('editar/<int:pk>/', (ProjetoUpdate.as_view()), name='projeto_editar'),
	# path('<int:pk>/deletar/', (Projeto_delete), name='projeto_deletar'),
	# path('detalhar/<int:pk>/', (ProjetoDetail.as_view()), name='projeto_detalhar'),
	# path('projeto-autocomplete', ion=True)(ProjetoAutocomplete.as_view()), name='projeto_autocomplete'),

	
]