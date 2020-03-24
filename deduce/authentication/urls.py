from django.urls import path
from .views import AuthComplete, LogoutSuccess, SignIn, TokenRefresh

urlpatterns = [
    path("signin", SignIn.as_view()),
]
