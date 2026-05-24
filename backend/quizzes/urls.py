from rest_framework.routers import DefaultRouter

from .views.question_view import QuestionViewSet
from .views.answer_view import UserAnswerViewSet

router = DefaultRouter()

router.register(
    r"questions",
    QuestionViewSet,
    basename="questions"
)

router.register(
    r"answers",
    UserAnswerViewSet,
    basename="answers"
)

urlpatterns = router.urls