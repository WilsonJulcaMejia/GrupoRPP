from .models import New

__author__ = 'lucaru9'

from rest_framework import serializers


class ListNewSerializer(serializers.ModelSerializer):
    class Meta:
        model = New
        fields = ('created_at', 'updated_at', 'title', 'sub_title', 'body', 'image', 'is_enabled')
