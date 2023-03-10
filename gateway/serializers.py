from rest_framework import serializers


class LoginSerializer(serializers.serializer):
    email = serializers.EmailField()
    password = serializers.CharField()