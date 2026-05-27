from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from content.models import (
    Topic, UserProgress
)

from quizzes.models import (
    Question, UserAnswer
)

class CompleteTopicView(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request):

        topic_id = request.data.get("topic_id")

        try:

            topic = Topic.objects.get(id=topic_id)

        except:

            return Response(
                {"error": "Topic not found"},
                status=status.HTTP_404_NOT_FOUND
            )
        
        total_questions = Question.objects.filter(
            topic=topic
        ).count()

        answered_questions = UserAnswer.objects.filter(
            user=request.user,
            question__topic=topic
        ).count()

        if answered_questions < total_questions:
            return Response(
                {
                    "error": (
                        "Answer all questions first"
                    )
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        
        progress, created = UserProgress.objects.update_or_create(
            user=request.user,
            topic=topic,
            defaults={
                "completed": True
            }
        )

        return Response(
            {
                "message": "Topic completed successfully"
            },
            status=status.HTTP_200_OK
        )

