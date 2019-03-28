from django.urls import path
from django.contrib.auth.decorators import permission_required
from .views import *

app_name = 'app'

urlpatterns = [
    path('', (Dashboard.as_view()), name='dashboard'),
]