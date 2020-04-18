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
        fields = (
            "level_number",
            "level_file_1",
            "level_file_2",
            "level_file_3",
            "cover_image",
            "question",
            "hints",
        )


class AnswerInputSerializer(serializers.Serializer):
    """Serialize input answer field."""

    answer = serializers.CharField(max_length=500)


class LeaderboardSerializer(serializers.ModelSerializer):
    """Serialize Leadeboard."""

    unlocked_by = serializers.CharField(source="unlocked_by.get_full_name")

    class Meta:
        model = Level
        fields = ("level_number", "unlocked_by")
