from django.urls import path
from .views import GetQuestion

urlpatterns = [
    path("question", GetQuestion.as_view()),
]
