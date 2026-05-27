from rest_framework import serializers

from content.models import Topic

from content.models import UserProgress

class TopicSerializer(serializers.ModelSerializer):

    locked = serializers.SerializerMethodField()

    class Meta:
        
        model = Topic
        
        fields = (
            "id",
            "title",
            "body",
            "order",
            "module",
            "locked",
        )

    def get_locked(self, obj):
        request = self.context.get("request")

        user = request.user

        # Primeiro tópico do módulo
        if obj.order == 1:
            
            previous_module = obj.module.order - 1
            # Primeiro módulo do sistema
            if previous_module <= 0:
                return False
            #Verifica se o módulo anterior foi concluido
            previous_topics_completed = UserProgress.objects.filter(
                user=user,
                topic__module__order=previous_module,
                completed=True
            ).count()
        
            previous_topics_total = Topic.objects.filter(
                module__order=previous_module
            ).count()

            return previous_topics_completed < previous_topics_total
        # Verifica tópico anterior
        previous_topics_completed = UserProgress.objects.filter(
            user=user,
            topic__module=obj.module,
            topic__order=obj.order - 1,
            completed=True
        ).exists()

        return not previous_topics_completed