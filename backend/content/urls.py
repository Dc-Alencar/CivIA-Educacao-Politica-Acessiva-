from rest_framework.routers import DefaultRouter

from content.views import CompleteTopicView

from django.urls import path

from content.views import (
    ModuleViewSet,
    TopicViewSet,
    UserProgressViewSet
)

router = DefaultRouter()

router.register(
    r"modules",
    ModuleViewSet,
    basename="modules"
)

router.register(
    r"topics",
    TopicViewSet,
    basename="topics"
)

router.register(
    r"progress",
    UserProgressViewSet,
    basename="progress"
)

urlpatterns = [
    path(
        "progress/complete-topic/",
        CompleteTopicView.as_view(),
        name="complete-topic"
    )
]

urlpatterns += router.urls