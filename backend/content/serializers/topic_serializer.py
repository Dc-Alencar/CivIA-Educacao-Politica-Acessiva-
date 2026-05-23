from rest_framework import serializers

from content.models import Topic

class TopicSerilizer(serializers.ModelSerializer):

    class Meta:
        
        model = Topic
        
        fields = "__all__"