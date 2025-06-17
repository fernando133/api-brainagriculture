from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from core.models import Produtor, Propriedade

class ProdutorAPITest(APITestCase):

    def setUp(self):
        self.produtor_data = {
            "nome": "Produtor Teste",
            "email": "produtor@email.com",
            "cidade": "Cidade X",
            "estado": "GO"
        }
        self.produtor = Produtor.objects.create(**self.produtor_data)

    def test_listar_produtores(self):
        url = reverse('produtor-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['nome'], self.produtor_data['nome'])

    def test_criar_produtor(self):
        url = reverse('produtor-list')
        data = {
            "nome": "Novo Produtor",
            "email": "novo@email.com",
            "cidade": "Cidade Y",
            "estado": "SP",
            "cpf": "529.982.247-25"  # CPF válido
        }

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Produtor.objects.count(), 2)

    def test_buscar_produtor_por_id(self):
        url = reverse('produtor-detail', args=[self.produtor.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['nome'], self.produtor_data['nome'])

    def test_atualizar_produtor(self):
        url = reverse('produtor-detail', args=[self.produtor.id])
        data = {
            "nome": "Produtor Atualizado",
            "email": "produtor@email.com",
            "cidade": "Cidade X",
            "estado": "GO",
            "cpf": "529.982.247-25"
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.produtor.refresh_from_db()
        self.assertEqual(self.produtor.nome, "Produtor Atualizado")

    def test_deletar_produtor(self):
        url = reverse('produtor-detail', args=[self.produtor.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Produtor.objects.count(), 0)

class DashboardAPITest(APITestCase):
    def test_dashboard_endpoint(self):
        url = reverse('dashboard')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
