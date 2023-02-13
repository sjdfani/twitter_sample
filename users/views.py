from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model
from django.utils import timezone
from .utils import get_tokens_for_user
from .serializer import (
    SignUpUserSerializer, SignInUserSerializer, UserSerializer,
)


class SignUpUser(CreateAPIView):
    serializer_class = SignUpUserSerializer
    queryset = get_user_model().objects.all()


class SignInUser(APIView):
    def post(self, request):
        serializer = SignInUserSerializer(
            data=request.data, context={'request': request}
        )
        if serializer.is_valid(raise_exception=True):
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            user = get_user_model().objects.get(username=username)
            if user.check_password(password):
                user.last_login = timezone.now()
                user.save()
                user_data = UserSerializer(user).data
                message = {
                    'user': user_data,
                    'tokens': get_tokens_for_user(user)
                }
                return Response(message, status=status.HTTP_200_OK)
            else:
                message = {'login': 'username or password is incorrect'}
                return Response(message, status=status.HTTP_401_UNAUTHORIZED)
