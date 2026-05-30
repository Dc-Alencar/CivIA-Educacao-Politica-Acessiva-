from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView

from accounts.serializers import RegisterSerializer

class RegisterView(APIView):

    permission_classes = [AllowAny]

    def post(self, request):

        serializer = RegisterSerializer(
            data=request.data
        )

        serializer.is_valid(
            raise_exception=True
        )

        user = serializer.save()

        refresh = RefreshToken.for_user(
            user
        )

        return Response(
            {
                "id": user.id,

                "username": user.username,

                "access": str(
                    refresh.access_token
                ),

                "refresh": str(
                    refresh
                )
            },
            status=status.HTTP_201_CREATED
        )
