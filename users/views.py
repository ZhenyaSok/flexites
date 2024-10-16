from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from users.models import User

class ActivateUsersView(APIView):
    """
    Представление для активации пользователя по ссылке из письма.
    """
    def get(self, request, uidb64, token, format=None):
        """
        Активация пользователя по ссылке из письма.
        """
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None
        if user is not None and default_token_generator.check_token(user, token):
            user.is_active = True
            user.save()
            return Response({'message': 'Поздравляем, Ваш аккаунт активирован!!!'},
                            status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Что-то пошло не так! Попробуйте снова!'},
                            status=status.HTTP_400_BAD_REQUEST)
