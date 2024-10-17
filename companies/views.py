from rest_framework import generics

from companies.models import Company
from companies.serializers import CompanySerializer


class CompanyListAPIView(generics.ListAPIView):
    """View для отображения списка организаций"""
    serializer_class = CompanySerializer
    queryset = Company.objects.all()

class CompanyCreateAPIView(generics.CreateAPIView):
    """View для добавления организации"""
    serializer_class = CompanySerializer
    queryset = Company.objects.all()

class CompanyRetrieveAPIView(generics.RetrieveAPIView):
    """View для отображения одной организации"""
    serializer_class = CompanySerializer
    queryset = Company.objects.all()