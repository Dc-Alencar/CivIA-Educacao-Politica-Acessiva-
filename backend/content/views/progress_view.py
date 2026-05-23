from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from content.models import UserProgress
from content.serializers import UserProgressSerializer

class UserProgressViewSet(viewsets.ModelViewSet):

    permission_classes = [IsAuthenticated]

    serializer_class = UserProgressSerializer

    def get_queryset(self):
        
        return UserProgress.objects.filter(
            user = self.request.user
        )
    
    def perform_create(self, serializer):
        
        serializer.save(
            user = self.request.user
        )