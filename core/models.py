# core/models.py
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


