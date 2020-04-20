from django.utils import timezone

from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import RetrieveAPIView, ListAPIView, GenericAPIView

from api.models import Level, AnswerLog, Hint, CurrentLevel
from api.serializers import (
    QuestionSerializer,
    AnswerInputSerializer,
    HintSerializer,
    LeaderboardSerializer,
    CurrentLevelSerializer,
)


class QuestionView(RetrieveAPIView):
    """Retrieve question based on current user level."""

    serializer_class = QuestionSerializer

    def get_queryset(self):
        current_level = CurrentLevel.objects.values_list("level", flat=True).first()
        # If this is the first question fetch request, so create the current level entry.
        if current_level == None:
            CurrentLevel.objects.create()
            return Level.objects.filter(level_number=1)
        return Level.objects.filter(level_number=current_level)

    def get_object(self):
        """Get question object."""
        return self.get_queryset().first()


class InputAnswerView(GenericAPIView):
    """Post and verify answers."""

    serializer_class = AnswerInputSerializer

    def post(self, request):
        serializer = AnswerInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        self.current_level = CurrentLevel.objects.values_list(
            "level", flat=True
        ).first()

        # Cannot answer a question if current_level is not set
        if self.current_level == None:
            return Response(
                {"message": "level_invalid"}, status=status.HTTP_400_BAD_REQUEST
            )

        answer_from_user = serializer.validated_data.get("answer")
        level_of_user = serializer.validated_data.get("level_number")

        self.log_answer(request, answer_from_user)
        self.add_answer_time(request)
        return self.verify_answer(request, answer_from_user, level_of_user)

    def log_answer(self, request, ans):
        """Log user responses."""
        AnswerLog.objects.create(
            user=request.user, level=self.current_level, answer=ans,
        )

    def add_answer_time(self, request):
        user = request.user
        user.last_anstime = timezone.now()
        user.save()

    def verify_answer(self, request, ans, level_of_user):
        """Verify if logged answer is correct."""
        level = self.get_object()

        if level is None:
            return Response(
                {"message": "level_invalid"}, status=status.HTTP_400_BAD_REQUEST
            )

        # If the level number sent from frontend does not match the current level number
        if level.level_number != level_of_user:
            return Response(
                {"message": "level has been solved"}, status=status.HTTP_400_BAD_REQUEST
            )

        user = request.user

        if level.answer.lower() == ans.lower():
            current_level_obj = CurrentLevel.objects.all().first()
            current_level_obj.level = self.current_level + 1
            current_level_obj.save()

            level.is_locked = False  # Unlock level for all users
            level.unlocked_by = user
            level.save()

            return Response({"correct_answer": True}, status=status.HTTP_200_OK)

        return Response({"correct_answer": False}, status=status.HTTP_200_OK)

    def get_queryset(self):
        return Level.objects.filter(level_number=self.current_level)

    def get_object(self):
        return self.get_queryset().first()


class LeaderboardView(ListAPIView):
    """Retrieve Leaderboard as a list."""

    serializer_class = LeaderboardSerializer

    def get_queryset(self):
        return Level.objects.filter(is_locked=False)


class CurrentLevelView(RetrieveAPIView):
    """Return the highest level that is locked"""

    serializer_class = CurrentLevelSerializer

    def get_queryset(self):
        return CurrentLevel.objects.all()

    def get_object(self):
        return self.get_queryset().first()
