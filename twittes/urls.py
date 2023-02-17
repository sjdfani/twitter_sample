from django.urls import path
from .views import (
    CreateTwittes, TwittesList, RetrieveUpdateDestroyTwittes, CreateLike, LikeList,
    DeleteLike, CreateComment, CommentList, CreateReTwittes, DeleteReTwittes,
)

app_name = 'twittes'

urlpatterns = [
    path('create/', CreateTwittes.as_view(), name='create_twittes'),
    path('list/', TwittesList.as_view(), name='twittes_list'),
    path('list/<int:pk>/', RetrieveUpdateDestroyTwittes.as_view(),
         name='retrieve_update_destroy_twittes'),
    path('like/create/', CreateLike.as_view(), name='create_like'),
    path('like/list/<int:pk>/', LikeList.as_view(),
         name='list_like'),  # pk of twittes
    path('like/delete/<int:pk>/', DeleteLike.as_view(),
         name='delete_like'),  # pk of twittes
    path('comment/create/', CreateComment.as_view(), name='create_comment'),
    path('comment/list/<int:pk>/', CommentList.as_view(),
         name='comment_list'),  # pk of twittes
    path('re-twittes/create/', CreateReTwittes.as_view(), name='create_reTwittes'),
    path('re-twittes/delete/<int:pk>/',
         DeleteReTwittes.as_view(), name='delete_reTwittes'),  # pk of twittes
]
