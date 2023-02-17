from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Twittes, Like, Comment
from .serializer import (
    TwittesSerializer, CreateTwittesSerializer, RetrieveUpdateDestroyTwittesSerializer,
    LikeSerializer, CreateLikeSerializer,
)


class CreateTwittes(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CreateTwittesSerializer
    queryset = Twittes.objects.all()


class TwittesList(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = TwittesSerializer

    def get_queryset(self):
        return Twittes.objects.filter(user=self.request.user)


class RetrieveUpdateDestroyTwittes(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return TwittesSerializer
        return RetrieveUpdateDestroyTwittesSerializer

    def get_queryset(self):
        return Twittes.objects.filter(user=self.request.user)


class CreateLike(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CreateLikeSerializer
    queryset = Like.objects.all()


class LikeList(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = LikeSerializer

    def get_queryset(self):
        pk = self.kwargs['pk']
        return Like.objects.filter(user=self.request.user, twittes__pk=pk)


class DeleteLike(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk, **kwargs):
        obj = Like.objects.filter(user=self.request.user, twittes__pk=pk)
        if obj.exists():
            obj.first().delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            message = {'obj': 'Not found'}
            return Response(message, status=status.HTTP_404_NOT_FOUND)
