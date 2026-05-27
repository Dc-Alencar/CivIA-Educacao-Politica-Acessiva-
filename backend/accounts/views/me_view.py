from rest_framework.views import APIView

from rest_framework.permissions import IsAuthenticated

from rest_framework.response import Response

from accounts.serializers.me_serializer import (
    MeSerializer
)

class MeView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):

        serializer = MeSerializer(
            request.user,
            context={
                "request": request
            }
        )

        return Response(serializer.data)