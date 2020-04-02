from rest_framework import serializers

from .models import Community


class CommunitySerializer(serializers.ModelSerializer):
    slug = serializers.CharField(allow_blank=True, required=False)
    name = serializers.CharField(allow_blank=True, required=False)
    instalaciones = serializers.BooleanField(required=False, default=False)

    class Meta:
        model = Community
        fields = ('slug', 'instalaciones', 'name')



