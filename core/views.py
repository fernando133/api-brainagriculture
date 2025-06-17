from django.shortcuts import render
from rest_framework import viewsets
from .models import Produtor, Propriedade, Safra, Cultura
from .serializers import ProdutorSerializer, PropriedadeSerializer, SafraSerializer, CulturaSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Sum, Count
import logging
logger = logging.getLogger(__name__)



class ProdutorViewSet(viewsets.ModelViewSet):
    queryset = Produtor.objects.all()
    serializer_class = ProdutorSerializer

class PropriedadeViewSet(viewsets.ModelViewSet):
    queryset = Propriedade.objects.all()
    serializer_class = PropriedadeSerializer

class SafraViewSet(viewsets.ModelViewSet):
    queryset = Safra.objects.all()
    serializer_class = SafraSerializer

class CulturaViewSet(viewsets.ModelViewSet):
    queryset = Cultura.objects.all()
    serializer_class = CulturaSerializer

class DashboardAPIView(APIView):
    def get(self, request):
        total_fazendas = Propriedade.objects.count()
        total_hectares = Propriedade.objects.aggregate(
            total_area=Sum('area_total_hectares')
        )['total_area'] or 0

        propriedades_por_estado = (
            Propriedade.objects
            .values('estado')
            .annotate(total=Count('id'))
            .order_by('-total')
        )

        culturas_por_tipo = (
            Cultura.objects
            .values('cultura_plantada')
            .annotate(total=Count('id'))
            .order_by('-total')
        )

        uso_solo = Propriedade.objects.aggregate(
            total_agricultavel=Sum('area_agriculturavel_hectares'),
            total_vegetacao=Sum('area_vegetacao_hectares')
        )

        return Response({
            "total_fazendas": total_fazendas,
            "total_hectares": total_hectares,
            "propriedades_por_estado": list(propriedades_por_estado),
            "culturas_por_tipo": list(culturas_por_tipo),
            "uso_do_solo": {
                "agricultavel": uso_solo['total_agricultavel'] or 0,
                "vegetacao": uso_solo['total_vegetacao'] or 0
            }
        })