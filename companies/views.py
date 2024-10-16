from rest_framework import generics

from companies.models import Company


class CompanyListAPIView(generics.ListAPIView):
    """View для отображения списка компаний"""
    serializer_class = CompanySerializer
    queryset = Company.objects.all()

class CompanyRetrieveAPIView(generics.RetrieveAPIView):
    """View для отображения одной компании"""
    serializer_class = CompanySerializer
    queryset = Company.objects.all()