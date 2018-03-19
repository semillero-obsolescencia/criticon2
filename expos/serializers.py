from django.contrib.auth.models import User
from rest_framework import serializers
from expos.models import Obra, Expo, Comentario



#class ComentarioSerializer(serializers.HyperlinkedModelSerializer):
class ComentarioSerializer(serializers.ModelSerializer):
  class Meta:
    model = Comentario
    fields = (
      'id',
      'obra',
      'texto'
    )

#class ObraSerializer(serializers.HyperlinkedModelSerializer):
class ObraSerializer(serializers.ModelSerializer):
    comentarios = ComentarioSerializer(many=True)
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
        'lecturas',
        'comentarios'
        )

#class ExpoSerializer(serializers.HyperlinkedModelSerializer):
class ExpoSerializer(serializers.ModelSerializer):
    obras = ObraSerializer(many=True)
    class Meta:
        model = Expo
        fields = (
          'id',
          'created',
          'titulo',
          'desde',
          'hasta',
          'lugar',
          'descripcion',
          'creditos',
          'texto_curatorial',
          'rating',
          'likes',
          'obras'
          )
