from rest_framework.decorators import api_view
from rest_framework.response import response
from rest_framework import status
from .serializers import UserSerializer


@api_view(["POST"])