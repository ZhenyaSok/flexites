from django.contrib.auth import get_user_model
from django.test import TestCase


class UsersManagersTests(TestCase):

    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(email="normal@user.ru", password="123qwe456asd", phone="+78525556363",
                                        first_name='Test1', last_name='Test_1ast')
        self.assertEqual(user.email, "normal@user.ru")
        self.assertTrue(user.is_active)
        self.assertEqual(user.role, "user")
        try:
            # имя пользователя имеет значение None для параметра AbstractUser
            # имя пользователя для опции AbstractBaseUser не существует
            self.assertIsNone(user.username)
        except AttributeError:
            pass
        with self.assertRaises(TypeError):
            User.objects.create_user()
        with self.assertRaises(TypeError):
            User.objects.create_user(email="")
        with self.assertRaises(ValueError):
            User.objects.create_user(email="", password="123qwe456asd", role='user', phone="+78525556363",
                                        first_name='Test1', last_name='Test_1ast')

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(email="super@user.ru",
                                                   first_name='Test', last_name='Test_last')
        self.assertEqual(admin_user.email, "super@user.ru")
        self.assertTrue(admin_user.is_active)
        self.assertEqual(admin_user.role, "admin")
        try:
            # имя пользователя имеет значение None для параметра AbstractUser
            # имя пользователя для опции AbstractBaseUser не существует
            self.assertIsNone(admin_user.username)
        except AttributeError:
            pass
        with self.assertRaises(ValueError):
            User.objects.create_superuser(email="", password="123qwe456asd", first_name='Test', last_name='Test_last')