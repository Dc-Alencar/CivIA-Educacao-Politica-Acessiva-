from rest_framework import viewsets

from content.models import UserProgress
from content.serializers import UserProgressSerializer

class UserProgressViewSet(viewsets.ModelViewSet):

    queryset = UserProgress.objects.all()

    serilizer_class = UserProgressSerializer