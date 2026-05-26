from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from quizzes.models import Question

from content.models import Topic

from quizzes.serializers import QuestionSerializer

class QuestionViewSet(viewsets.ReadOnlyModelViewSet):

    serializer_class = QuestionSerializer

    permission_classes = [IsAuthenticated]

    def get_queryset(self):

        queryset = Question.objects.all()

        module_order = self.request.query_params.get(
            "module_order"
        )

        topic_order = self.request.query_params.get(
            "topic_order"
        )

        if module_order:

            queryset = queryset.filter(
                topic__module__order=module_order
            )

        if topic_order:

            queryset = queryset.filter(
                topic__order=topic_order
            )

        return queryset.order_by("id")