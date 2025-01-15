from django.urls import path
from .views import chat_view, sign_up

urlpatterns = [
    path('', chat_view, name='chat_view'),
    path('sign-up/', sign_up, name='sign_up'),
]
