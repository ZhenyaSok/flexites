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
    """Модель пользователя
    Абстрактный базовый класс,
    требуется адрес электронной почты и пароль. Остальные поля являются необязательными."""

    username = None
    email = models.EmailField(unique=True, verbose_name='Email')
    first_name = models.CharField(max_length=50, verbose_name='Имя', **NULLABLE)
    last_name = models.CharField(max_length=75, verbose_name='Фамилия', **NULLABLE)
    phone = PhoneNumberField(region='KZ', **NULLABLE)
    image = ResizedImageField(size=[200, 200], upload_to='avatars', **NULLABLE) # уменьшение картинки
    companies = models.ManyToManyField(Company, verbose_name='Список организаций', **NULLABLE)
    role = models.CharField(max_length=5, choices=UserRoles.choices, default='user', verbose_name='статус пользователя')
    is_active = models.BooleanField(default=True, verbose_name='активен/не активен')

    USERNAME_FIELD = 'email'  # эта константа определяет поле для логина пользователя
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone']  # эта константа содержит список с полями,
    # которые необходимо заполнить при создании пользователя

    @property
    def is_superuser(self):
        """Пользователь - суперюзер, если его роль == 'admin'"""
        return self.is_admin

    @property
    def is_staff(self):
        """Пользователь - сотрудник, если его роль == 'admin'"""
        return self.is_admin

    def has_perm(self, perm, obj=None):
        """У пользователя есть определённые разрешения, если его роль == 'admin'"""
        return self.is_admin

    def has_module_perms(self, app_label):
        """ У пользователя есть разрешения на просмотр приложения app_label,
        если его роль == 'admin'"""
        return self.is_admin

    # Переопределение менеджера модели пользователя
    objects = UserManager()

    @property
    def is_admin(self):
        """Пользователь - суперюзер, если его роль == 'admin"""
        return self.role == UserRoles.ADMIN

    @property
    def is_user(self):
        """ Обычный пользователь, если роль == 'user' """
        return self.role == UserRoles.USER

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'