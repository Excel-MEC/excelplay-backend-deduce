import requests

from django.conf import settings
from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status

from api.models import User
from api.serializers import AccessTokenSerializer, ProfileSerializer


class LoginApiView(APIView):
    """Create or get an user object by exchanging Auth0 access_token."""

    permission_classes = (AllowAny,)

    def post(self, request):
        """Post auth0 access token, returns a jwt refresh_token ."""
        serializer = AccessTokenSerializer(data=request.data)

        if serializer.is_valid():
            access_token = serializer.validated_data.get("access_token", None)
            print(access_token)
            return self.verify_access_token(access_token)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def verify_access_token(self, access_token):
        """Verify if auth0 access_token is valid."""
        header = {
            "Authorization": "Bearer " + access_token,
        }
        response = requests.get(url=settings.AUTH0_URL, headers=header)

        if response.status_code == 200:
            user_data = response.json()
            user = self.create_or_get_user(user_data)
            token = user.create_refresh_token()
            return Response(token, status=status.HTTP_200_OK)

        return Response(response.content, status=status.HTTP_401_UNAUTHORIZED)

    def create_or_get_user(self, user_data):
        """Create or get a user object using user_id."""
        user_data_sub = user_data.get("sub").split("|")[
            1
        ]  # Unique user_id from 0Auth provider
        user, created = User.objects.get_or_create(
            id=user_data_sub,
            first_name=user_data.get("given_name", ""),
            last_name=user_data.get("family_name", ""),
            email=user_data.get("email", ""),
            profile_picture=user_data.get("picture", ""),
            username=user_data.get("email"),
        )
        if created:
            user.set_unusable_password()
            user.save()
        return user


class ProfileView(RetrieveAPIView):
    serializer_class = ProfileSerializer

    def get_queryset(self):
        return self.request.user
    
    def get_object(self):
        return self.get_queryset()