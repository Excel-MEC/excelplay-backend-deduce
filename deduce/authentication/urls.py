from django.urls import path
from .views import AuthComplete, LogoutSuccess

urlpatterns = [
    # Only for testing purposes, remove this later.
    # Configure auth0 redirect to the public facing URL of the frontend landing page before deploying
    "authcomplete",
    AuthComplete.as_view(),
    "logoutsuccess",
    LogoutSuccess.as_view(),
]
