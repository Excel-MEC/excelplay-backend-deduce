from django.urls import path
from .views import AuthComplete

urlpatterns = ["authcomplete", AuthComplete.as_view()]
