from rest_framework import serializers

from user_management.models import User
from user_management.models.user_profile import GENDER_CHOICES


class SignupTenantRequestSerializer(serializers.Serializer):
    email = serializers.EmailField()
    first_name = serializers.CharField(max_length=100, min_length=3)
    last_name = serializers.CharField(max_length=100, min_length=3)
    password = serializers.CharField(max_length=100, min_length=8)
    gender = serializers.ChoiceField(choices=GENDER_CHOICES)

    def validate_email(self, value):
        user = User.objects.filter(email=value).first()

        if user:
            raise serializers.ValidationError("Account with this Email already exists")

        return value
