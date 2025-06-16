# core/serializers.py
from rest_framework import serializers
from .models import Produtor

class ProdutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produtor
        fields = '__all__'

    def validate(self, data):
        cpf_raw = data.get('cpf')
        cnpj_raw = data.get('cnpj')

        if not cpf_raw and not cnpj_raw:
            raise serializers.ValidationError("Informe um CPF ou um CNPJ.")

        if cpf_raw:
            if not Produtor.validar_cpf(cpf_raw):
                raise serializers.ValidationError({"cpf": "CPF inválido."})
            data['cpf'] = Produtor.limpar_cpf(cpf_raw)

        if cnpj_raw:
            if not Produtor.validar_cnpj(cnpj_raw):
                raise serializers.ValidationError({"cnpj": "CNPJ inválido."})
            data['cnpj'] = Produtor.limpar_cnpj(cnpj_raw)

        return data
