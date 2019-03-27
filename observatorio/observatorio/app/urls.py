from django.urls import path
from .views import IndexView
from django.contrib.auth.decorators import permission_required
from .views import *

app_name = 'app'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
]