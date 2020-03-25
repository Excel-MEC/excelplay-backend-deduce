from rest_framework import serializers
from .models import Level


class AccessTokenSerializer(serializers.Serializer):
    """Serialize Auth0 access_token."""

    access_token = serializers.CharField(max_length=32)


class QuestionSerializer(serializers.ModelSerializer):
    """Serialize Question."""

    class Meta:
        model = Level
        fields = ("level_number", "level_file", "question", "filetype")
