from django.conf import settings
from rest_framework.response import Response
from rest_framework import status

import jwt


def is_logged_in(fn):
    # Decorator to check if user has sent a valid JWT with the request
    def wrapper_fn(self, req):
        key = req.headers.get("Authorization")
        if not key:
            return Response("Not Authorized", status.HTTP_401_UNAUTHORIZED)
        key = key.split(" ")
        if len(key) != 2:
            return Response("Not Authorized", status.HTTP_401_UNAUTHORIZED)
        key = key[1]
        try:
            jwt_data = jwt.decode(key, settings.JWT_SECRET_KEY, algorithm="HS512")
            return fn(self, req, jwt_data)
        except Exception as e:
            return Response("Invalid token", status.HTTP_401_UNAUTHORIZED)

    return wrapper_fn
