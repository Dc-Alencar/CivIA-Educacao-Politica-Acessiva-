from rest_framework import serializers

from accounts.models import User

import re

class RegisterSerializer(serializers.ModelSerializer):

    password = serializers.CharField(
        write_only = True
    )

    class Meta:

        model = User

        fields = (
            "id",
            "username",
            "password",
        )
    
    # Valida se senha cumpre os requistios mínimos:
    # - Mínimo de 8 caracteres
    # - Pelo menos 1 caractere especial
    # - Pelo menos 1 número
    def validate_password(self, value):

        # mínimo 8 caracteres
        if len(value) < 8:

            raise serializers.ValidationError(
                "A senha deve conter pelo menos 8 caracteres."
            )

        # pelo menos 1 número
        if not re.search(r"\d", value):

            raise serializers.ValidationError(
                "A senha deve conter pelo menos 1 número."
            )

        # pelo menos 1 caractere especial
        if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", value):

            raise serializers.ValidationError(
                "A senha deve conter pelo menos 1 caractere especial."
            )

        return value
    
    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data["username"],
            password=validated_data["password"],
        )

        return user