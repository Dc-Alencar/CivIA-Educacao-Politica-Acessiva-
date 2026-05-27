from rest_framework import serializers

from quizzes.models import Alternative

class AlternativeSerializer(serializers.ModelSerializer):

    class Meta:

        model = Alternative 

        fields = (
            "id",
            "text",
        )