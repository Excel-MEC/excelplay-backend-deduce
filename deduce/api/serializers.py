from rest_framework import serializers
from .models import Level


class AccessTokenSerializer(serializers.Serializer):
    access_token = serializers.CharField(max_length=32)


class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = ("level_number", "level_file", "question", "filetype")
