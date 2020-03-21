from django.db.models import F
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import DeduceUser, Level, AnswerLog, Hint
from .serializers import LevelSerializer
from datetime import datetime


class GetQuestion(APIView):
    def get(self, req):
        user_id = "123"
        duser, created = DeduceUser.objects.get_or_create(user_id=user_id)
        level = Level.objects.get(level_number=duser.level)
        if not level:
            return Response(
                "Internal Server Error", status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
        szr = LevelSerializer(level)
        return Response(szr.data, status=status.HTTP_200_OK)


class Answer(APIView):
    def post(self, req):
        # Format of POST request should be {"answer": "attempt"}
        if "answer" not in req.data:
            return Response("Invalid request", status=status.HTTP_400_BAD_REQUEST)

        user_id = "123"
        duser = DeduceUser.objects.get(user_id=user_id)
        if not duser:
            return Response("Invalid Credentials", status=status.HTTP_401_UNAUTHORIZED)
        level = Level.objects.get(level_number=duser.level)
        AnswerLog.objects.create(
            user=duser,
            anstime=datetime.now(),
            level=duser.level,
            answer=req.data["answer"],
        )
        if level.answer == req.data["answer"]:
            duser.level = F("level") + 1
            duser.last_anstime = datetime.now()
            duser.save()
            return Response("correct", status=status.HTTP_200_OK)
        return Response("incorrect", status=status.HTTP_200_OK)
