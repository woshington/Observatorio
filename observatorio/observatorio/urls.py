from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('observatorio.app.urls', namespace='app')),
    path('projeto/', include('observatorio.projeto.urls', namespace='projeto')),
]
# Servindo arquivos static em modo DEBUG=True
if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)