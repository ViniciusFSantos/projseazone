from rest_framework import serializers
from core.models import Anuncios


class AnunciosSerializer(serializers.ModelSerializer):
  class Meta:
    model = Anuncios
    fields = '__all__'