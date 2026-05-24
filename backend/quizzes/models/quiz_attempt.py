from django.conf import settings
from django.db import models

from content.models import Topic

class QuizAttempt(models.Model):
    
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="quiz_attempts"
    )

    topic = models.ForeignKey(
        Topic,
        on_delete=models.CASCADE,
        related_name="attempts"
    )

    score = models.FloatField(
        default=0
    )

    passed = models.BooleanField(
        default=False
    )

    created_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):

        return f"{self.user.username} - {self.topic.title}"