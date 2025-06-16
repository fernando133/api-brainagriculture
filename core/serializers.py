# core/serializers.py
from rest_framework import serializers
from .models import Produtor, Propriedade

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

class PropriedadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Propriedade
        fields = '__all__'

    def validate(self, data):
        valido, mensagem = Propriedade.validar_areas(
            area_total=data.get("area_total_hectares"),
            area_agriculturavel=data.get("area_agriculturavel_hectares"),
            area_vegetacao=data.get("area_vegetacao_hectares")
        )
        if not valido:
            raise serializers.ValidationError(mensagem)
        return data