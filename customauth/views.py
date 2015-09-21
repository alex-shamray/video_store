# Avoid shadowing the login() and logout() views below.
from django.contrib.auth import (login as auth_login,
                                 logout as auth_logout)
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


class RegisterView(APIView):
    """
    Handles the register action.
    """
    user_creation_form = UserCreationForm

    def post(self, request, format=None):
        form = self.user_creation_form(request.data)
        if form.is_valid():
            form.save()

            return Response({})
        return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    """
    Handles the login action.
    """
    authentication_form = AuthenticationForm

    def post(self, request, format=None):
        form = self.authentication_form(request, data=request.data)
        if form.is_valid():
            # Log the user in.
            auth_login(request, form.get_user())

            content = {
                'user': unicode(request.user),
                'auth': unicode(request.auth),
            }
            return Response(content)
        return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)


class LogoutView(APIView):
    """
    Logs out the user.
    """
    permission_classes = (IsAuthenticated,)

    def post(self, request, format=None):
        auth_logout(request)

        content = {
            'user': unicode(request.user),
            'auth': unicode(request.auth),
        }
        return Response(content)
