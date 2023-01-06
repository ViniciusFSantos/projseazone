from .serializers import ImoveisSerializer
from rest_framework import generics
from core.models import Imoveis
from django_filters.rest_framework import DjangoFilterBackend


class ImoveisListView(generics.ListCreateAPIView):
  queryset = Imoveis.objects.all()
  serializer_class = ImoveisSerializer
  filter_backends = [DjangoFilterBackend]
  filterset_fields = ['imovel_codigo','limite_hospedes','banheiros_quant','permite_animais','valor_limpeza','data_ativa']

class ImoveisDetailView(generics.RetrieveUpdateDestroyAPIView):
  serializer_class = ImoveisSerializer
  queryset = Imoveis.objects.all()
  