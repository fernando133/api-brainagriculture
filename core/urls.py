from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProdutorViewSet, PropriedadeViewSet, SafraViewSet, CulturaViewSet
from .views import DashboardAPIView

router = DefaultRouter()
router.register(r'produtores', ProdutorViewSet)
router.register(r'propriedades', PropriedadeViewSet)
router.register(r'safras', SafraViewSet)
router.register(r'culturas', CulturaViewSet)
urlpatterns = [
    path('', include(router.urls)),
    path('dashboard/', DashboardAPIView.as_view(), name='dashboard'),
]
