from rest_framework import serializers

from django.contrib.auth.models import User



class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True, write_only=True)


class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True, write_only=True)

    def validation_username(self, value):
        if User.objects.filter(username=value):
            raise serializers.ValidationError('A user with that username already exists.')  # username valid deyilsə xəta verir
        return value
