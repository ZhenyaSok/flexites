from rest_framework import serializers
from companies.models import Company

class CompanySerializer(serializers.ModelSerializer):
    '''Сериалайзер для отображения списка организаций и одной организации'''
    class Meta:
        model = Company
        fields = "__all__"
