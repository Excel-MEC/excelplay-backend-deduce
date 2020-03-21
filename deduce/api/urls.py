from django.urls import path
from .views import GetQuestion, Answer

urlpatterns = [
    path("question", GetQuestion.as_view()),
    path("answer", Answer.as_view()),
]
