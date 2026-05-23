from rest_framework import viewsets

from content.models import Topic
from content.serializers import TopicSerializer

class TopicViewSet(viewsets.ModelViewSet):
    
    queryset = Topic.objects.all()

    serilizer_class = TopicSerializer
