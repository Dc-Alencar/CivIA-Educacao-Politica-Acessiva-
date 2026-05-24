from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from quizzes.models import UserAnswer
from quizzes.serializers import UserAnswerSerializer

class UserAnswerViewSet(viewsets.ModelViewSet):

    serializer_class = UserAnswerSerializer

    permission_classes = [IsAuthenticated]

    def get_queryset(self):

        return UserAnswer.objects.filter(
            user=self.request.user
        )

    def perform_create(self, serializer):

        alternative = serializer.validated_data[
            "selected_alternative"
        ]

        serializer.save(
            user=self.request.user,
            is_correct=alternative.is_correct
        )