from django.contrib.auth.models import (
    BaseUserManager
)

class UserManager(BaseUserManager):
    """Менеджер модели пользователя, где адрес электронной почты является уникальным идентификатором
    для аутентификации вместо имен пользователей."""

    def create_user(self, email, first_name, last_name, phone, role="user", password=None):
        """Создание пользователя"""
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            role=role,
            is_active=True
        )
        user.is_active = True
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, first_name, last_name, password=None, phone=None):
        """Функция для создания суперпользователя"""

        user = self.create_user(
            email,
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            password=password,
            role="admin"
        )

        user.save(using=self._db)
        return user