from django.urls import path
from .views import (
    SignUpUser, SignInUser,
)

app_name = 'users'

urlpatterns = [
    path('sign-up/', SignUpUser.as_view(), name='sign_up_user'),
    path('sign-in/', SignInUser.as_view(), name='sign_in_user')
]
