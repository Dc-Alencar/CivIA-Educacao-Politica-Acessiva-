from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from quizzes.models import Question

from content.models import Topic

from quizzes.serializers import QuestionSerializer

import random

from rest_framework.response import Response

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

        # Filtra por módulo
        if module_order:

            queryset = queryset.filter(
                topic__module__order=module_order
            )

        # Filtra por tópico
        if topic_order:

            queryset = queryset.filter(
                topic__order=topic_order
            )

        return queryset
    
    # Aleatoriza as questões e filtra o número de questões na requisição
    def list(self, request, *args, **kwargs):

        queryset = list(self.get_queryset())

        random.shuffle(queryset)

        limit = request.query_params.get("limit")

        if limit:

            try:
                queryset = queryset[:int(limit)]
            except ValueError:
                pass

        serializer = self.get_serializer(
            queryset,
            many=True
        )

        return Response(serializer.data)