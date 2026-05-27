from django.urls import path

from .views import RegisterView, MeView

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
    )
]