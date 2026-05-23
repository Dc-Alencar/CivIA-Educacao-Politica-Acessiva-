from rest_framework.routers import DefaultRouter

from content.views import (
    ModuleViewSet,
    TopicViewSet,
    UserProgressViewSet
)

router = DefaultRouter()

router.register(
    r"modules",
    ModuleViewSet
)

router.register(
    r"topics",
    TopicViewSet
)

router.register(
    r"progress",
    UserProgressViewSet,
    basename="progress"
)

urlpatterns = router.urls