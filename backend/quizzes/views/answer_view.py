from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from quizzes.models import UserAnswer
from quizzes.serializers import UserAnswerSerializer

from content.models.user_progress import UserProgress

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

        question = serializer.validated_data[
            "question"
        ]

        answer, created = UserAnswer.objects.update_or_create(
            user=self.request.user,

            question=question,

            defaults={
                "selected_alternative": alternative,
                "is_correct": alternative.is_correct
            }
        )

        topic = question.topic

        total_question = topic.questions    .count()

        answered_questions = UserAnswer.objects.filter(
            
            user=self.request.user,

            question__topic=topic
            
        ).count()

        if answered_questions >= total_question:

            UserProgress.objects.update_or_create(

                user=self.request.user,

                topic=topic,

                defaults={
                    "completed": True
                }
            )