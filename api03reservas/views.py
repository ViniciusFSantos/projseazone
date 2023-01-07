from .serializers import ReservasSerializer
from rest_framework import generics
from core.models import Reservas
from django_filters.rest_framework import DjangoFilterBackend


class ReservasListView(generics.ListCreateAPIView):
  
  queryset = Reservas.objects.all()
  serializer_class = ReservasSerializer
  filter_backends = [DjangoFilterBackend]
  filterset_fields = ['reserva_anuncio', 'reserva_codigo', 'chekin_data', 'chekout_data', 'valor_total', 'quant_hospedes', 'comentarios']

class ReservasDetailView(generics.RetrieveDestroyAPIView):
  
  serializer_class = ReservasSerializer
  queryset = Reservas.objects.all()