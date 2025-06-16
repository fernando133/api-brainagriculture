from django.shortcuts import render
from rest_framework import viewsets
from .models import Produtor, Propriedade
from .serializers import ProdutorSerializer, PropriedadeSerializer

class ProdutorViewSet(viewsets.ModelViewSet):
    queryset = Produtor.objects.all()
    serializer_class = ProdutorSerializer

class PropriedadeViewSet(viewsets.ModelViewSet):
    queryset = Propriedade.objects.all()
    serializer_class = PropriedadeSerializer