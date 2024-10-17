from rest_framework import serializers
from companies.models import Company
from users.models import User


class CompanySerializer(serializers.ModelSerializer):
    '''Сериалайзер для отображения списка организаций и одной организации'''
    list_users = serializers.SerializerMethodField()

    def get_list_users(self, company):
        """Метод выводит все уроки в курсе"""
        return [f"{user.first_name} {user.last_name}" for user in User.objects.filter(companies=company)]
    class Meta:
        model = Company
        fields = "__all__"
