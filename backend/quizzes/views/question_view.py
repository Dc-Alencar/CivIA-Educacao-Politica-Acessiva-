from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from quizzes.models import Question
from quizzes.serializers import QuestionSerializer

class QuestionViewSet(viewsets.ReadOnlyModelViewSet):

    serializer_class = QuestionSerializer

    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        
        queryset = Question.objects.all()

        topic_id = self.request.query_params.get("topic")

        if topic_id:

            queryset = queryset.filter(
                topic_id=topic_id
            )

        return queryset