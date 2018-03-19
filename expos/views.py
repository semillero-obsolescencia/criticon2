from django.contrib.auth.models import User
from django.shortcuts import render
from django.template import RequestContext, loader

from expos.models import Obra, Expo, Comentario
from expos.serializers import ExpoSerializer, ObraSerializer, ComentarioSerializer
from expos.permissions import IsOwnerOrReadOnly

from rest_framework import generics, permissions, renderers, viewsets
from rest_framework.response import Response
from rest_framework.decorators import detail_route


# Create your views here.

class ExpoViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides 'list', 'create', 'retrieve',
    'update', and 'destroy' actions.
    """
    queryset = Expo.objects.all()
    serializer_class = ExpoSerializer


class ObraViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides 'list', 'create', 'retrieve',
    'update', and 'destroy' actions.
    """
    queryset = Obra.objects.all()
    serializer_class = ObraSerializer

class ComentarioViewSet(viewsets.ModelViewSet):
  queryset = Comentario.objects.all()
  serializer_class = ComentarioSerializer


def index(request):
    return render(request,
        'expos/index.html',
        {'context_instance': RequestContext(request, {})}
    )
