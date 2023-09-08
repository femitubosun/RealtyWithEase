from rest_framework import serializers


class ChangePasswordRequestSerializer(serializers.Serializer):
    old_password = serializers.CharField()
    new_password = serializers.CharField()
