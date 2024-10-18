from pictures.conf import get_settings

from users.apps import UsersConfig
from django.urls import include, path

from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from users.views import ActivateUsersView, ResetPasswordUsersView

users_router = SimpleRouter()

app_name = UsersConfig.name


urlpatterns = [

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),

    path('activate/<uidb64>/<token>/', ActivateUsersView.as_view(), name='activate_user'), # активация с почты по ссылке
    path('reset_password_confirm/{uid}/{token}/', ResetPasswordUsersView.as_view(), name='reset_password_confirm')

    # auth/users/ авторизация пользователя
    # auth/users/me/ get,put,patch просмотр, редактирование пользователя (передается: токен, и изменяемые поля)
    # auth/jwt/create/ создание токенов
    # auth/jwt/refresh/
    # auth/users/reset_password/ сброс пароля, на почту приходит письмо со ссылкой
    # auth/users/reset_password_confirm/  (входные данные, метод POST: uid, token, new_password,  re_new_password)
    # auth/users/set_password/ изменить пароль,(входные данные, new_password, re_new_password, current_password)

]
