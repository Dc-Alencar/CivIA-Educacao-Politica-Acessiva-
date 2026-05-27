from django.urls import path

from ai_assistant.views.chat_view import (
    ChatView
)

urlpatterns = [
    
    path(
        "chat/",
        ChatView.as_view(),
        name="ai_assistant-chat"
    )
]
