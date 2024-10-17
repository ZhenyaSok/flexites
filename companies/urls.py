from django.urls import path
from companies.apps import CompaniesConfig
from companies.views import (CompanyListAPIView, CompanyRetrieveAPIView, CompanyCreateAPIView)

app_name = CompaniesConfig.name

urlpatterns = [

    path('list/', CompanyListAPIView.as_view(), name='list'),
    path('create/', CompanyCreateAPIView.as_view(), name='create'),
    path('detail/<int:pk>/', CompanyRetrieveAPIView.as_view(), name='detail'),

]
