from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

# from deduce.api.views import GetQuestion, Answer
from api.views.auth import LoginApiView
from api.views.level import QuestionView, InputAnswerView

urlpatterns = [
    path("login", LoginApiView.as_view()),
    path("refresh", TokenRefreshView.as_view(), name="token_refresh"), # return access_token
    path("question", QuestionView.as_view(), name="get-question"),
    path("answer", InputAnswerView.as_view(), name="input-answer"),
]
