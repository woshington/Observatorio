from django.views.generic import TemplateView
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required, permission_required
from django.db import IntegrityError, transaction
from django.urls import reverse, reverse_lazy


from django.db.models import Avg, Min, Max, Sum

@method_decorator(login_required, name='dispatch')
class IndexTeste(TemplateView):
    template_name = 'index.html'