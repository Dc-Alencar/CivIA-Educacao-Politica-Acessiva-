from django.urls import path

from .views import RegisterView, MeView

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)

urlpatterns = [
    # url de registro de usuários
    path(
        "register/",
        RegisterView.as_view(),
        name="register"
    ),

    # URL de regaste de dados do usuário
    path(
        "me/",
        MeView.as_view(),
        name="me"
    ),

    path(
        "login/",
        TokenObtainPairView.as_view(),
        name="token_obtain_pair"
    ),

    path(
        "refresh/",
        TokenRefreshView.as_view(),
        name="token_refresh"
    ),
]