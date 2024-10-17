from pictures.conf import get_settings

from users.apps import UsersConfig
from django.urls import include, path

from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from users.views import ActivateUsersView

users_router = SimpleRouter()

app_name = UsersConfig.name


urlpatterns = [

    # path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),

    path('activate/<uidb64>/<token>/', ActivateUsersView.as_view(), name='activate_user'), # активация с почты по ссылке

    # auth/users/ авторизация пользователя
    # auth/users/me/ get,put,patch просмотр, редактирование пользователя (передается: токен, и изменяемые поля)
    # auth/users/resend_activation/ повторная отправка ссылки на почту для регистрации
    # auth/jwt/create/ создание токенов
    # auth/jwt/refresh/
    # auth/users/reset_password/ сброс пароля
    # auth/users/set_password/ изменить пароль
    # path(r'^auth/', include('djoser.urls')),
]
