from companies.models import Company
from users.models import User

from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
class CompanyTestCase(APITestCase):

    def setUp(self) -> None:
        self.user = User.objects.create_user(
            email='test@test',
            password='tes2test',
            first_name='Testt',
            last_name='Testt',
            phone="+78889995252",
        )
        self.client.force_authenticate(user=self.user)
        self.company = Company.objects.create(title='Test_company')
    def test_company_list(self):
        """Список компаний"""

        response = self.client.get(reverse('companies:list'),)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_company(self):
        """Тест создания организации (create)"""
        data = {'title': 'Test001'}

        response = self.client.post(reverse('companies:create'), data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_company(self):
        """Тест просмотра организации (retrieve)"""
        response = self.client.get(reverse('companies:detail', args=[self.company.id]))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
