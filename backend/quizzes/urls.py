from rest_framework.routers import DefaultRouter

from django.urls import path

from .views import (
    QuestionViewSet,
    UserAnswerViewSet,
    SubmitQuizView
)

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

urlpatterns = [

    path(
        "submit/",
        SubmitQuizView.as_view(),
        name="submit-quiz"
    )
]

urlpatterns += router.urls