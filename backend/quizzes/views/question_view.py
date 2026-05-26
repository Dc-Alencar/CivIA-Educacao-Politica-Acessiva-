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

        limit = self.request.query_params.get(
            "limit"
        )
        
        # filtra por módulo
        if module_order:

            queryset = queryset.filter(
                topic__module__order=module_order
            )
            
        # filtra por tópico
        if topic_order:

            queryset = queryset.filter(
                topic__order=topic_order
            )
        
        queryset = queryset.order_by("id")

        # Limita quantidade
        if limit:

            try:
                queryset = queryset[:int(limit)]

            except ValueError:
                pass

        return queryset