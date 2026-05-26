from rest_framework import serializers


class AnswerItemSerializer(serializers.Serializer):

    question = serializers.IntegerField()

    selected_alternative = serializers.IntegerField()


class SubmitQuizSerializer(serializers.Serializer):

    module_order = serializers.IntegerField()

    topic_order = serializers.IntegerField()

    answers = AnswerItemSerializer(
        many=True
    )