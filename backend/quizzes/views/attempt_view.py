from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from quizzes.models import QuizAttempt
from quizzes.serializers import QuizAttemptSerializer

class QuizAttemptViewSet(viewsets.ModelViewSet):

    serializer_class = QuizAttemptSerializer

    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return QuizAttempt.objects.filter(
            user=self.request.user
        )
    
    def perform_create(self, serializer):
        serializer.save(
            user=self.request.user
        )