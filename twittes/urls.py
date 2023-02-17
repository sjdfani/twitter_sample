from django.urls import path
from .views import (
    CreateTwittes, TwittesList, RetrieveUpdateDestroyTwittes, CreateLike, LikeList,
    DeleteLike,
)

app_name = 'twittes'

urlpatterns = [
    path('create/', CreateTwittes.as_view(), name='create_twittes'),
    path('list/', TwittesList.as_view(), name='twittes_list'),
    path('list/<int:pk>/', RetrieveUpdateDestroyTwittes.as_view(),
         name='retrieve_update_destroy_twittes'),
    path('like/create/', CreateLike.as_view(), name='create_like'),
    path('like/list/<int:pk>/', LikeList.as_view(), name='list_like'),
    path('like/delete/<int:pk>/', DeleteLike.as_view(), name='delete_like'),
]
