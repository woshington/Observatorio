
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('projeto_estevao.core.urls', namespace='core')),
    path('accounts/', include('projeto_estevao.accounts.urls', namespace='accounts')),
]
# Servindo arquivos static em modo DEBU=True
if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
