from django.conf import settings
from django.db import models

from .question import Question
from .alternative import Alternative
from .quiz_attempt import QuizAttempt

class UserAnswer(models.Model):
    
    attempt = models.ForeignKey(
        QuizAttempt,
        on_delete=models.CASCADE,
        related_name="answers"
    )

    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        related_name="answers"
    )

    selected_alternative = models.ForeignKey(
        Alternative,
        on_delete=models.CASCADE
    )

    answered_at = models.DateTimeField(
        auto_now=True
    )

    is_correct = models.BooleanField(
        default=False
    )

    def __str__(self):

        return f"{self.attempt.user.username} - {self.question.id}"