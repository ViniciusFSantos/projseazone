from rest_framework import serializers
from core.models import Imoveis


class ImoveisSerializer(serializers.ModelSerializer):
  class Meta:
    model = Imoveis
    fields = '__all__'