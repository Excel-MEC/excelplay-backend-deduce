from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response


class AuthComplete(APIView):
    def get(self, req):
        return Response("Login successful")


class LogoutSuccess(APIView):
    def get(self, req):
        return Response("Logout successful")
