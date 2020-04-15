from rest_framework import serializers
from .models import Level, Hint


class AccessTokenSerializer(serializers.Serializer):
    """Serialize Auth0 access_token."""

    access_token = serializers.CharField(max_length=32)


class HintSerializer(serializers.ModelSerializer):
    """Serialize Hints"""

    class Meta:
        model = Hint
        fields = ("hint",)


class QuestionSerializer(serializers.ModelSerializer):
    """Serialize Question."""

    hints = HintSerializer(many=True, read_only=True)

    class Meta:
        model = Level
        fields = ("level_number", "level_file", "cover_image", "question", "filetype", "hints")


class AnswerInputSerializer(serializers.Serializer):
    """Serialize input answer field."""
    
    answer = serializers.CharField(max_length=500)
