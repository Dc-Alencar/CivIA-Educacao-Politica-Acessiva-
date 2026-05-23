from django.db import models
from django.conf import settings

from .topic import Topic

class UserProgress(models.Model):
    STATUS_CHOICES = [
        ('NOT_STARTED', 'Not started'),
        ('IN_PROGRESS', 'In progress'),
        ('DONE', 'Done')
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="progress"
    )

    topic = models.ForeignKey(
        Topic,
        on_delete=models.CASCADE,
        related_name="progress"
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="NOT_STARTED"
    )

    completed_at = models.DateTimeField(
        null=True,
        blank=True
    )

    last_acessed_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ("user", "topic")
        
    def __str__(self):

        return f"{self.user.username} - {self.topic.title}"