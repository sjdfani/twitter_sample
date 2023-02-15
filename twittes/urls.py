from django.urls import path
from .views import (
    CreateTwittes, TwittesList, RetrieveUpdateDestroyTwittes,
)

app_name = 'twittes'

urlpatterns = [
    path('create/', CreateTwittes.as_view(), name='create_twittes'),
    path('list/', TwittesList.as_view(), name='twittes_list'),
    path('list/<int:pk>/', RetrieveUpdateDestroyTwittes.as_view(),
         name='retrieve_update_destroy_twittes'),
]
