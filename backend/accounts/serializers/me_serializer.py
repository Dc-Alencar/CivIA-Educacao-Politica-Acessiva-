from rest_framework import serializers

from content.models import Module

from content.serializers.module_progress_serializer import (
    ModuleProgressSerializer
)

class MeSerializer(serializers.Serializer):

    id = serializers.IntegerField()

    username = serializers.CharField()

    modules = serializers.SerializerMethodField()

    def get_modules(self, obj):

        modules = Module.objects.all().order_by("order")

        serializer = ModuleProgressSerializer(
            modules,
            many=True,
            context=self.context
        )

        return serializer.data