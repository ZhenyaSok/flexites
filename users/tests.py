from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APITestCase
from authentications.email import EMAILS

User = get_user_model()

class UserViewSetTest(APITestCase):

    def setUp(self):
        """
        Set up method which is used to initialize before any test run.
        """
        self.user_info = self.generate_user_info()

    def generate_user_info(self):
        """Generate user data for new user.
        Returns:
            Dict: dictionary of the test user data.
        """
        return {
            "first_name": "fake.first_name()",
            "last_name": "fake.last_name()",
            "username": "fake.user_name()",
            "password": "fake.password()",
        }

    def test_create_user(self):
        """
        Test for creating users using API.
        """
        url = reverse("user-list")
        response = self.client.post(
            url,
            self.user_info,
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        user = User.objects.get(id=response.data['id'])
        self.assertEqual(user.email, self.user_info["email"])
        self.assertEqual(user.username, self.user_info["username"])
        # self.assertEqual(user.ssn, self.user_info["ssn"])
        self.assertTrue(user.password is not self.user_info["password"])
        self.assertTrue(user.is_deleted is not True)
        self.assertTrue(user.father_first_name is None)
        self.assertTrue(user.mother_first_name is None)
        self.assertTrue(user.password is not None)
        self.assertTrue(user.birth_date is not None)

    def test_get_token(self):
        """
        This test is used to test the login API. getting token and testing the token.
        """
        # Create a new user to login
        user_info = self.generate_user_info()
        new_user = self.client.post(
            reverse("user-list"),
            user_info,
        )
        self.assertEqual(new_user.status_code, status.HTTP_201_CREATED)

        # Activation of User
        from authentications.email import EMAILS

        activation_url = reverse('user-activation')
        activation_data = EMAILS[user_info["email"]]
        self.client.post(activation_url, activation_data)

        url = reverse("jwt-create")
        data = {
            "username": user_info["username"],
            "password": user_info["password"],
        }
        response = self.client.post(url, data)

        self.assertTrue(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data["access"] is not None)

    def test_get_user(self):
        """
        This test for retrieving single user using API.
        """

        # Create a new user to login
        new_user = self.client.post(
            reverse("user-list"),
            self.user_info,
        )
        self.assertEqual(new_user.status_code, status.HTTP_201_CREATED)

        # Activate User


        activation_url = "http://127.0.0.1:8000/auth/users/activation/"
        activation_data = EMAILS[self.user_info["email"]]
        self.client.post(activation_url, activation_data)

        # Get token
        url = reverse("jwt-create")
        data = {
            "username": self.user_info["username"],
            "password": self.user_info["password"],
        }

        response = self.client.post(url, data)
        self.assertTrue(response.status_code, status.HTTP_200_OK)

        # Get user
        token = response.data["access"]
        self.client.credentials(HTTP_AUTHORIZATION=f"JWT {token}")

        url = reverse('user-list', kwargs={'id':new_user.data["id"]})
        get_user = self.client.get(url)

        self.assertEqual(get_user.status_code, status.HTTP_200_OK)
        self.assertEqual(get_user.data["id"], new_user.data["id"])
        self.assertEqual(get_user.data["email"], new_user.data["email"])

        test_user = self.client.post(
            reverse("user-list"),
            self.generate_user_info(),
        )
        url = reverse('user-list', kwargs={'id': test_user.data['id'] })
        get_user = self.client.get(url)
        self.assertEqual(get_user.status_code, status.HTTP_404_NOT_FOUND)


from django.contrib.auth import get_user_model
from django.test import TestCase


class UsersManagersTests(TestCase):

    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(email="normal@user.ru", password="123qwe456asd")
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
            User.objects.create_user(email="", password="123qwe456asd", role='user')

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(email="super@user.ru", password="456qwe123asd")
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
            User.objects.create_superuser(email="", password="123qwe456asd", role='admin')