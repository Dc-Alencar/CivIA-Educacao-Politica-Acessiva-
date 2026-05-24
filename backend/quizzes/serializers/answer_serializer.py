from rest_framework import serializers

from quizzes.models import (
    UserAnswer,
    Alternative
)

class UserAnswerSerializer(serializers.ModelSerializer):

    class Meta:
        
        model = UserAnswer

        fields = (
            "id",
            "attempt",
            "question",
            "selected_alternative",
            "is_correct",
            "answered_at",
        )

        read_only_fields = (
            "is_correct",
            "answered_at",
        )

    def validate(self, attrs):

        question = attrs["question"]
    
        alternative = attrs["selected_alternative"]

        if alternative.question != question:

            raise serializers.ValidationError(
                "Alternative does not belong to this question"
            )
        
        return attrs