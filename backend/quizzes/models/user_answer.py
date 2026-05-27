from django.conf import settings
from django.db import models

from .question import Question
from .alternative import Alternative

class UserAnswer(models.Model):
    
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
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
    
    class Meta:

        unique_together = ("user", "question")

    def __str__(self):

        return f"{self.user.username} - {self.question.id}"