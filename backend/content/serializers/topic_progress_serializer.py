from rest_framework import serializers

from content.models import (
    Topic,
    UserProgress,
    Module
)

class TopicProgressSerializer(serializers.ModelSerializer):

    completed = serializers.SerializerMethodField()

    locked = serializers.SerializerMethodField()

    class Meta:

        model = Topic

        fields = (
            "id",
            "title",
            "order",
            "completed",
            "locked",
        )

    def get_completed(self, obj):

        user = self.context["request"].user

        return UserProgress.objects.filter(
            user=user,
            topic=obj,
            completed=True
        ).exists()
    
    def get_locked(self, obj):

        user = self.context["request"].user

        # Primeiro tópico do módulo
        if obj.order == 1:

            previous_module_order = obj.module.order - 1

            # Primeiro módulo do sistema
            if previous_module_order <= 0:
                return False

            previous_module = Module.objects.filter(
                order=previous_module_order
            ).first()

            if not previous_module:
                return False

            previous_topics = Topic.objects.filter(
                module=previous_module
            )

            completed_topics = UserProgress.objects.filter(
                user=user,
                topic__in=previous_topics,
                completed=True
            ).count()

            return completed_topics < previous_topics.count()

        # Outros tópicos
        previous_topic = Topic.objects.filter(
            module=obj.module,
            order=obj.order - 1
        ).first()

        if not previous_topic:
            return True

        previous_completed = UserProgress.objects.filter(
            user=user,
            topic=previous_topic,
            completed=True
        ).exists()

        return not previous_completed