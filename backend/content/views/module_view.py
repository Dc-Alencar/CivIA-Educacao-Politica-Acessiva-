from rest_framework import viewsets

from content.models import Module
from content.serializers import ModuleSerializer

class ModuleViewSet(viewsets.ModelViewSet):
    
    queryset = Module.objects.all()

    serializer_class = ModuleSerializer
