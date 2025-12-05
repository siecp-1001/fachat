from django.urls import path
from .views import chat_page, advanced_chat

urlpatterns = [
    path("", chat_page, name="chat_page"),      # Frontend page: /chat/
    path("ask/", advanced_chat, name="chat_api") # API endpoint: /chat/ask/
]
