from django.urls import path
from .views import (
    CreateTwittes, TwittesList, RetrieveUpdateDestroyTwittes,
)

app_name = 'twittes'

urlpatterns = [
    path('create/', CreateTwittes.as_view(), name='create-twittes'),
    path('list/', TwittesList.as_view(), name='twittes-list'),
    path('list/<int:pk>/', RetrieveUpdateDestroyTwittes.as_view(),
         name='retrieve-update-destroy-twittes'),
]
