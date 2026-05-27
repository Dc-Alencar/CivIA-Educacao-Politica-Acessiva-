from rest_framework import serializers

from quizzes.models import Question

from .alternative_serializer import AlternativeSerializer

class QuestionSerializer(serializers.ModelSerializer):

    alternatives = AlternativeSerializer(
        many=True,
        read_only=True
    )

    class Meta:

        model = Question

        fields = (
            "id",
            "text",
            "alternatives",
        )