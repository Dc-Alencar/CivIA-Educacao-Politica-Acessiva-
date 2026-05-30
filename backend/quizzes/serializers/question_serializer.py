from rest_framework import serializers

from quizzes.models import Question

from .alternative_serializer import AlternativeSerializer

import random

class QuestionSerializer(serializers.ModelSerializer):

    alternatives = serializers.SerializerMethodField()

    class Meta:

        model = Question

        fields = (
            "id",
            "text",
            "alternatives",
        )

    def get_alternatives(self, obj):

        alternatives = list(
            obj.alternatives.all()
        )

        random.shuffle(alternatives)

        return AlternativeSerializer(
            alternatives,
            many=True
        ).data