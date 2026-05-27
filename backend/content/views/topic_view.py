from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from content.models import Topic
from content.serializers import TopicSerializer

class TopicViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = Topic.objects.all()

    serializer_class = TopicSerializer

    permission_classes = [IsAuthenticated]
