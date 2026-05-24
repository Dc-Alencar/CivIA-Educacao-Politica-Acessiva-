from rest_framework.routers import DefaultRouter

from .views.question_view import QuestionViewSet
from .views.answer_view import UserAnswerViewSet
from .views.attempt_view import QuizAttemptViewSet

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

router.register(
    r"attempts",
    QuizAttemptViewSet,
    basename="attempts"
)

urlpatterns = router.urls