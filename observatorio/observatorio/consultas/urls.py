from django.urls import path
from django.contrib.auth.decorators import permission_required
from .views import *

app_name = 'consultas'

urlpatterns = [
    path('orcamento-maior-que', (OrcamentoMaiorQue.as_view()), name='orcamento_maior_que'),
]