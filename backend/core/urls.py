from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

urlpatterns = [

    path('admin/', admin.site.urls),

    path("api-auth/", include("rest_framework.urls")),

    path("api/accounts/", include("accounts.urls")),

    path("api/content/", include("content.urls")),

    path("api/quizzes/", include("quizzes.urls")),

    path(
        "api/ai_assistant/",
        include("ai_assistant.urls")
    ),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) # Adicionar Isto
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # Adicionar Isto