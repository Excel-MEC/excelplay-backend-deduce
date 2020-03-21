from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework import status
from .models import DeduceUser, Level, AnswerLog, Hint
from .serializers import LevelSerializer


class GetQuestion(GenericAPIView):
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
