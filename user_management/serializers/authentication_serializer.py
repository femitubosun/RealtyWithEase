from rest_framework import serializers

from user_management.models import User


class AuthenticateUserSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate_email(self, value):
        user = User.objects.filter(email=value).first()

        if not user:
            raise serializers.ValidationError("Invalid Credentials")

        return value
