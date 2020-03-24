from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

import requests

from .models import User


class SignIn(APIView):
    def post(self, req):
        data = req.data

        if "access_token" in data:
            access_token = data["access_token"]
        else:
            return Response("Authentication failed", status.HTTP_401_UNAUTHORIZED)

        try:
            # Send the access_token to auth0 to obtain user info
            r = requests.get(
                "http://agzuniverse.auth0.com/userinfo",
                header={"Authorization": "Bearer {0}".format(access_token)},
            )
            userinfo = r.json()

            # userinfo['sub'] is the unique ID for that user
            userinfo["sub"] = userinfo["sub"].split("|")[1]

            # If the user does not exist, create a new user
            curruser = User.objects.get(id=userinfo["sub"])
            if not curruser:
                curruser = User.objects.create(
                    id=userinfo["sub"],
                    name=userinfo["name"],
                    pro_pic=userinfo["picture"],
                    email=userinfo["email"],
                )
            req.session["user"] = curruser.id
            req.session["logged_in"] = True
            req.session.save()

            return Response("Login success", status.HTTP_200_OK)

        except Exception as e:
            return Response(
                "Authentication failed", status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class AuthComplete(APIView):
    def get(self, req):
        return Response("Login successful")


class LogoutSuccess(APIView):
    def get(self, req):
        return Response("Logout successful")
