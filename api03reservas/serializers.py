from rest_framework import serializers
from core.models import Reservas


class ReservasSerializer(serializers.ModelSerializer):
  
  class Meta:
    model = Reservas
    fields = '__all__'
    
  def validar_data(self, data):

    if data['chekin_data'] > data['chekout_data']:
        raise serializers.ValidationError("Data de ChekOut deve ser posterior a data de ChekIn")
    return data