from .serializers import AnunciosSerializer
from rest_framework import generics
from core.models import Anuncios
from django_filters.rest_framework import DjangoFilterBackend


class AnunciosListView(generics.ListCreateAPIView):
  queryset = Anuncios.objects.all()
  serializer_class = AnunciosSerializer
  filter_backends = [DjangoFilterBackend]
  filterset_fields = ['anuncio_imovel', 'plataforma', 'taxa_cobrada']

class AnunciosDetailView(generics.RetrieveUpdateAPIView):
  serializer_class = AnunciosSerializer
  queryset = Anuncios.objects.all()
  