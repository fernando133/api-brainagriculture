from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProdutorViewSet, PropriedadeViewSet

router = DefaultRouter()
router.register(r'produtores', ProdutorViewSet)
router.register(r'propriedades', PropriedadeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
