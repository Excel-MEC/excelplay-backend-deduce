from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from api.views.auth import LoginApiView
from api.views.level import QuestionView, InputAnswerView, HintView

urlpatterns = [
    path("login", LoginApiView.as_view(), name="deduce-login"),
    path("refresh", TokenRefreshView.as_view(), name="deduce-token-refresh"),
    path("question", QuestionView.as_view(), name="deduce-question"),
    path("answer", InputAnswerView.as_view(), name="deduce-answer"),
    path("hint", HintView.as_view(), name="deduce-hint"),
]
