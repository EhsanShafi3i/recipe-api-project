"""views for the user API."""

from rest_framework import generics

from .serializers import UserSerializer


class CreateUserView(generics.CreateAPIView):
    """Create Api for user creation."""

    serializer_class = UserSerializer
