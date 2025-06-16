# core/models.py
from django.db import models
from validate_docbr import CPF, CNPJ

from django.db import models
from validate_docbr import CPF, CNPJ

class Produtor(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=2)  
    cpf = models.CharField(max_length=14, blank=True, null=True, unique=True)   
    cnpj = models.CharField(max_length=18, blank=True, null=True, unique=True)

    def __str__(self):
        return self.nome

    @staticmethod
    def limpar_cpf(cpf_raw: str) -> str:
        return cpf_raw.replace(".", "").replace("-", "")

    @staticmethod
    def limpar_cnpj(cnpj_raw: str) -> str:
        return cnpj_raw.replace(".", "").replace("/", "").replace("-", "")

    @staticmethod
    def validar_cpf(cpf_raw: str) -> bool:
        cpf = Produtor.limpar_cpf(cpf_raw)
        return CPF().validate(cpf)

    @staticmethod
    def validar_cnpj(cnpj_raw: str) -> bool:
        cnpj = Produtor.limpar_cnpj(cnpj_raw)
        return CNPJ().validate(cnpj)

    @staticmethod
    def msg_cpf_ou_cnpj_obrigatorio() -> str:
        return "Informe um CPF ou um CNPJ."

    @staticmethod
    def msg_cpf_invalido() -> str:
        return "CPF inválido."

    @staticmethod
    def msg_cnpj_invalido() -> str:
        return "CNPJ inválido."


class Propriedade(models.Model):
    id = models.AutoField(primary_key=True)
    produtor = models.ForeignKey(Produtor, related_name='propriedades', on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=2)
    area_total_hectares = models.DecimalField(max_digits=10, decimal_places=2)
    area_agriculturavel_hectares = models.DecimalField(max_digits=10, decimal_places=2)
    area_vegetacao_hectares = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.nome} ({self.produtor.nome})"

    @staticmethod
    def validar_areas(area_total, area_agriculturavel, area_vegetacao):
        if (area_agriculturavel + area_vegetacao) > area_total:
            return False
        return True
    
    @staticmethod
    def msg_erro_areas_invalidas() -> str:
        return "A soma das áreas agricultável e de vegetação não pode exceder a área total da propriedade."



