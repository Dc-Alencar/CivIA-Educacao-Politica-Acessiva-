from rest_framework import serializers

from content.models import (
    Module,
    Topic,
    UserProgress
)

from content.serializers.topic_progress_serializer import (
    TopicProgressSerializer
)


class ModuleProgressSerializer(serializers.ModelSerializer):

    topics = serializers.SerializerMethodField()

    completed = serializers.SerializerMethodField()

    class Meta:

        model = Module

        fields = (
            "id",
            "title",
            "order",
            "completed",
            "topics",
        )

    def get_topics(self, obj):

        topics = Topic.objects.filter(
            module=obj
        ).order_by("order")

        serializer = TopicProgressSerializer(
            topics,
            many=True,
            context=self.context
        )

        return serializer.data

    def get_completed(self, obj):

        user = self.context["request"].user

        topics = Topic.objects.filter(
            module=obj
        )

        total = topics.count()

        completed = UserProgress.objects.filter(
            user=user,
            topic__in=topics,
            completed=True
        ).count()

        return total > 0 and total == completed