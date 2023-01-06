from . import views
from django.urls import path, include


urlpatterns = [
    path('', views.IndexView.as_view(), name = 'index'),
    path('imoveis/', include('api01imoveis.urls')),
    path('anuncios/', include('api02anuncios.urls')),
    path('reservas/', include('api03reservas.urls')),
]

