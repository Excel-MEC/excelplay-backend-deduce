from django.urls import path
from .views import AuthComplete, LogoutSuccess, SignIn, TokenRefresh

urlpatterns = [
    path("token", SignIn.as_view()),
]
