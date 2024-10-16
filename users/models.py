from django.contrib.auth.models import AbstractBaseUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from companies.models import Company
from django.utils.translation import gettext_lazy as _
'''
Пользователь:
- Емайл
- Пароль
- Фамилия
- Имя
- Телефон
- Аватар(фотография).
- Связь на список организаций(может быть больше одной)
*Базовые (технические) поля django, кроме логина, он не должен использоваться'''
NULLABLE = {"null": True, "blank": True}

class UserRoles(models.TextChoices):
    """Enum-класс для пользователя"""
    USER = 'user', _('user')
    ADMIN = 'admin', _('admin')


class User(AbstractBaseUser):
    """Модель пользователя"""

    username = None
    email = models.EmailField(unique=True, verbose_name='Email', **NULLABLE)
    first_name = models.CharField(max_length=50, verbose_name='Имя', **NULLABLE)
    last_name = models.CharField(max_length=75, verbose_name='Фамилия', **NULLABLE)
    phone = PhoneNumberField(max_length=35, verbose_name='номер телефона', **NULLABLE)
    image = models.ImageField(upload_to='user/', verbose_name='Фото', **NULLABLE)
    companies = models.ManyToManyField(Company, verbose_name='Список организаций', **NULLABLE)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'