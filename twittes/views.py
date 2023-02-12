from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from .models import Twittes
from .serializer import (
    TwittesSerializer, CreateTwittesSerializer, RetrieveUpdateDestroyTwittesSerializer,
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
