from rest_framework import generics
from rest_framework.permissions import AllowAny

from accounts.models import User
from accounts.serializers import RegisterSerializer

class RegisterView(generics.CreateAPIView):

    queryset = User.objects.all()

    serializer_class = RegisterSerializer

    permission_classes = [AllowAny]
