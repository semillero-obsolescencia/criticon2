from django.contrib.auth.models import User
from rest_framework import serializers
from expos.models import Obra, Expo

class ExpoSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Expo
        fields = ('id',
          'created',
          'titulo',
          'desde',
          'hasta',
          'lugar',
          'descripcion',
          'creditos',
          'texto_curatorial',
          'rating',
          'likes')

class ObraSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Obra
        fields = (
        'id',
        'created',
        'expo',
        'creador',
        'titulo',
        'fecha',
        'medio',
        'descripcion',
        'rating',
        'likes',
        'lecturas'
        )
