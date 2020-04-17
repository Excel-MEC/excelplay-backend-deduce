from datetime import datetime

from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import RetrieveAPIView, ListAPIView, GenericAPIView

from api.models import Level, AnswerLog, Hint
from api.serializers import QuestionSerializer, AnswerInputSerializer, HintSerializer, LeaderboardSerializer


class QuestionView(RetrieveAPIView):
    """Retrieve question based on current user level."""

    serializer_class = QuestionSerializer

    def get_queryset(self):
        user_level = self.request.user.level
        return Level.objects.filter(level_number=user_level)

    def get_object(self):
        """Get question object."""
        return self.get_queryset().first()


class InputAnswerView(GenericAPIView):
    """Post and verify answers."""

    serializer_class = AnswerInputSerializer
    def post(self, request):
        serializer = AnswerInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        self.log_answer(request, serializer)
        self.add_answer_time(request)
        return self.verify_answer(request, serializer)

    def log_answer(self, request, serializer):
        """Log user responses."""
        AnswerLog.objects.create(
            user=request.user,
            level=request.user.level,
            answer=serializer.data.get("answer"),
        )

    def add_answer_time(self, request):
        user = request.user
        user.last_anstime = datetime.now()
        user.save()

    def verify_answer(self, request, serializer):
        """Verify if logged answer is correct."""
        level = self.get_object()
        user = request.user
        user_answer = serializer.data.get("answer")

        if level.answer.lower() == user_answer.lower():
            user.level += 1
            user.save()

            level.is_locked = False  # Unlock level for all users
            level.unlocked_by = user
            level.save()

            return Response({"correct_answer": True}, status=status.HTTP_200_OK)

        return Response({"correct_answer": False}, status=status.HTTP_200_OK)

    def get_queryset(self):
        return Level.objects.filter(level_number=self.request.user.level)

    def get_object(self):
        return self.get_queryset().first()


class LeaderboardView(ListAPIView):
    """Retrieve Leaderboard as a list."""

    serializer_class = LeaderboardSerializer
    def get_queryset(self):
        return Level.objects.filter(is_locked=False)