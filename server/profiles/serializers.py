from rest_framework import serializers

from .models import Propietario, Inquilino
from ..authentication.serializers import ProfileSerializer


class PropietarioSerializer(serializers.ModelSerializer):
    user = ProfileSerializer(read_only=True)
    bankAccount = serializers.CharField(allow_blank=True)
    isAdmin = serializers.BooleanField()
    isPresident = serializers.BooleanField()

    class Meta:
        model = Propietario
        fields = ('user', 'isPresident', 'isAdmin', 'bankAccount')

    def create(self, validated_data):
        user = self.context.get('user', None)
        prop = Propietario.objects.create(user=user, **validated_data)

        return prop


class InquilinoSerializer(serializers.ModelSerializer):
    user = ProfileSerializer(read_only=True)
    bankAccount = serializers.CharField(allow_blank=True)
    canPublish = serializers.BooleanField()

    class Meta:
        model = Inquilino
        fields = ('user', 'canPublish', 'bankAccount')

    def create(self, validated_data):
        user = self.context.get('user', None)
        prop = Inquilino.objects.create(user=user, **validated_data)

        return prop
