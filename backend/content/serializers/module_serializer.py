from rest_framework import serializers

from content.models import Module

class ModuleSerilizer(serializers.ModelSerializer):

    class Meta:
        
        model = Module
        
        fields = "__all__"