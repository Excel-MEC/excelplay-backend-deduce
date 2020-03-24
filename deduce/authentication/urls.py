from django.urls import path
# from .views import AuthComplete, LogoutSuccess, SignIn, TokenRefresh
from .views import SignIn

urlpatterns = [
    path("signin", SignIn.as_view()),
]
