from django.contrib.auth.models import AbstractBaseUser
from django.db import models
from .managers import UserManager
from companies.models import Company
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _
from django_resized import ResizedImageField

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
    phone = PhoneNumberField(region='KZ', **NULLABLE)
    image = ResizedImageField(size=[200, 200], upload_to='avatars', **NULLABLE) # уменьшение картинки
    companies = models.ManyToManyField(Company, verbose_name='Список организаций', **NULLABLE)
    role = models.CharField(max_length=5, choices=UserRoles.choices, default='user', verbose_name='статус пользователя')
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone']

    @property
    def is_superuser(self):
        return self.is_admin

    @property
    def is_staff(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin

    objects = UserManager()

    @property
    def is_admin(self):
        return self.role == UserRoles.ADMIN

    @property
    def is_user(self):
        return self.role == UserRoles.USER

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'