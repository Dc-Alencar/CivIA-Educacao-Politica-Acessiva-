from rest_framework import serializers

from quizzes.models import QuizAttempt

class QuizAttemptSerializer(serializers.ModelSerializer):

    class Meta:

        model = QuizAttempt

        fields = (
            "id",
            "topic",
            "score",
            "passed",
            "created_at",
        )

        read_only_fields = (
            "score",
            "passed",
            "created_at",
        )