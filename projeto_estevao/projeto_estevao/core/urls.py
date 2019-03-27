
from django.urls import path
from django.contrib.auth.decorators import permission_required
from .views import *

app_name = 'core'

urlpatterns = [
    # path('', IndexTeste.as_view(), name='index'),
    path('', permission_required('core:index', raise_exception=True)(IndexTeste.as_view()), name='index'),

]
