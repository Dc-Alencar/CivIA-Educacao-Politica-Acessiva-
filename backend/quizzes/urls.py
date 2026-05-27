from rest_framework.routers import DefaultRouter

from django.urls import path

from .views import (
    QuestionViewSet,
    UserAnswerViewSet,
    SubmitQuizView
)

router = DefaultRouter()

# url de questões
router.register(
    r"questions",
    QuestionViewSet,
    basename="questions"
)

# url de respostas : INATIVA, não use
router.register(
    r"answers",
    UserAnswerViewSet,
    basename="answers"
)

urlpatterns = [

    # url de envio de respostas dos quizzes
    path(
        "submit/",
        SubmitQuizView.as_view(),
        name="submit-quiz"
    )
]

urlpatterns += router.urls