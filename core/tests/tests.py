from django.test import TestCase
from core.models import Produtor, Propriedade, Safra, Cultura

class ProdutorModelTest(TestCase):

    def test_limpar_cpf(self):
        raw_cpf = '123.456.789-09'
        expected = '12345678909'
        self.assertEqual(Produtor.limpar_cpf(raw_cpf), expected)

    def test_limpar_cnpj(self):
        raw_cnpj = '12.345.678/0001-95'
        expected = '12345678000195'
        self.assertEqual(Produtor.limpar_cnpj(raw_cnpj), expected)

    def test_validar_cpf_valido(self):
        cpf = '529.982.247-25'
        self.assertTrue(Produtor.validar_cpf(cpf))

    def test_validar_cpf_invalido(self):
        cpf = '111.111.111-11'
        self.assertFalse(Produtor.validar_cpf(cpf))

    def test_validar_cnpj_valido(self):
        cnpj = '04.252.011/0001-10'
        self.assertTrue(Produtor.validar_cnpj(cnpj))

    def test_validar_cnpj_invalido(self):
        cnpj = '04.252.011/0001-00'
        self.assertFalse(Produtor.validar_cnpj(cnpj))


    def test_msg_cpf_ou_cnpj_obrigatorio(self):
        self.assertEqual(
            Produtor.msg_cpf_ou_cnpj_obrigatorio(),
            "Informe um CPF ou um CNPJ."
        )

    def test_msg_cpf_invalido(self):
        self.assertEqual(
            Produtor.msg_cpf_invalido(),
            "CPF inválido."
        )

    def test_msg_cnpj_invalido(self):
        self.assertEqual(
            Produtor.msg_cnpj_invalido(),
            "CNPJ inválido."
        )

class PropriedadeModelTest(TestCase):
    def setUp(self):
        # Criar um produtor para usar nos relacionamentos
        self.produtor = Produtor.objects.create(
            nome="Produtor Teste",
            email="produtor@email.com",
            cidade="Cidade X",
            estado="GO"
        )

    def test_validar_areas_valido(self):
        total = 100
        agriculturavel = 60
        vegetacao = 40
        self.assertTrue(Propriedade.validar_areas(total, agriculturavel, vegetacao))

    def test_validar_areas_invalido(self):
        total = 100
        agriculturavel = 70
        vegetacao = 40
        self.assertFalse(Propriedade.validar_areas(total, agriculturavel, vegetacao))

    def test_msg_erro_areas_invalidas(self):
        self.assertEqual(
            Propriedade.msg_erro_areas_invalidas(),
            "A soma das áreas agricultável e de vegetação não pode exceder a área total da propriedade."
        )

    def test_str_repr(self):
        propriedade = Propriedade.objects.create(
            produtor=self.produtor,
            nome="Fazenda Primavera",
            cidade="Cidade Y",
            estado="GO",
            area_total_hectares=100,
            area_agriculturavel_hectares=60,
            area_vegetacao_hectares=40
        )
        self.assertEqual(str(propriedade), "Fazenda Primavera (Produtor Teste)")

class SafraCulturaModelTest(TestCase):
    def setUp(self):
        self.produtor = Produtor.objects.create(
            nome="Produtor Teste",
            email="produtor@email.com",
            cidade="Cidade X",
            estado="GO"
        )
        self.propriedade = Propriedade.objects.create(
            produtor=self.produtor,
            nome="Fazenda Primavera",
            cidade="Cidade Y",
            estado="GO",
            area_total_hectares=100,
            area_agriculturavel_hectares=60,
            area_vegetacao_hectares=40
        )

    def test_criar_safra(self):
        safra = Safra.objects.create(
            propriedade=self.propriedade,
            ano="2024"
        )
        self.assertEqual(safra.propriedade, self.propriedade)
        self.assertEqual(safra.ano, "2024")

    def test_criar_cultura(self):
        safra = Safra.objects.create(
            propriedade=self.propriedade,
            ano="2024"
        )
        cultura = Cultura.objects.create(
            safra=safra,
            cultura_plantada="Soja"
        )
        self.assertEqual(cultura.safra, safra)
        self.assertEqual(cultura.cultura_plantada, "Soja")