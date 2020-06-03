from rest_framework import serializers
from .models import Level, Hint, CurrentLevel, User


class AccessTokenSerializer(serializers.Serializer):
    """Serialize Auth0 access_token."""

    access_token = serializers.CharField(max_length=32)


class ProfileSerializer(serializers.ModelSerializer):
    """Serialize profile info"""

    name = serializers.CharField(source="get_full_name")

    class Meta:
        model = User
        fields = ("id", "name", "email", "profile_picture", "score")


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
            "score",
            "cover_image",
            "question",
            "hints",
        )


class AnswerInputSerializer(serializers.Serializer):
    """Serialize input answer field."""

    answer = serializers.CharField(max_length=500)
    level_number = serializers.IntegerField()


class LeaderboardSerializer(serializers.ModelSerializer):
    """Serialize Leadeboard."""

    unlocked_by = serializers.CharField(source="unlocked_by.get_full_name")
    profile_picture = serializers.CharField(source="unlocked_by.profile_picture")
    score = serializers.IntegerField(source="unlocked_by.score")

    class Meta:
        model = Level
        fields = ("level_number", "unlocked_by", "profile_picture", "score")


class CurrentLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CurrentLevel
        fields = ("level",)
