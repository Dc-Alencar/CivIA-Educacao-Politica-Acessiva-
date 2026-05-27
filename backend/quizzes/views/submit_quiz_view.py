from rest_framework.views import APIView

from rest_framework.permissions import (
    IsAuthenticated
)

from rest_framework.response import Response

from rest_framework import status

from quizzes.serializers import (
    SubmitQuizSerializer
)

from quizzes.models import (
    Question,
    Alternative,
    UserAnswer
)

from content.models import (
    Topic,
    UserProgress,
    Module
)

class SubmitQuizView(APIView):

    permission_classes = [IsAuthenticated]

    # Verifica se o tópico está desbloqueado
    def is_topic_unlocked(self, user, topic):

        # PRIMEIRO TÓPICO DO PRIMEIRO MÓDULO
        if topic.module.order == 1 and topic.order == 1:
            return True

        # PRIMEIRO TÓPICO DE UM MÓDULO
        if topic.order == 1:

            previous_module = Module.objects.filter(
                order=topic.module.order - 1
            ).first()

            if not previous_module:
                return False

            previous_topics = Topic.objects.filter(
                module=previous_module
            )

            completed_count = UserProgress.objects.filter(
                user=user,
                topic__in=previous_topics,
                completed=True
            ).count()

            return completed_count == previous_topics.count()

        # OUTROS TÓPICOS DO MESMO MÓDULO
        previous_topic = Topic.objects.filter(
            module=topic.module,
            order=topic.order - 1
        ).first()

        if not previous_topic:
            return False

        return UserProgress.objects.filter(
            user=user,
            topic=previous_topic,
            completed=True
        ).exists()

    def post(self, request):

        serializer = SubmitQuizSerializer(
            data=request.data
        )

        serializer.is_valid(
            raise_exception=True
        )

        data = serializer.validated_data

        module_order = data["module_order"]

        topic_order = data["topic_order"]

        answers = data["answers"]

        # Busca tópico
        topic = Topic.objects.filter(
            module__order=module_order,
            order=topic_order
        ).first()

        if not topic:

            return Response(
                {
                    "detail": "Tópico não encontrado."
                },
                status=status.HTTP_404_NOT_FOUND
            )
        
        # Verifica desbloqueio
        is_unlocked = self.is_topic_unlocked(
            request.user,
            topic
        )

        if not is_unlocked:
            return Response(
                {
                    "detail": "Tópico bloqueado."
                },
                status=status.HTTP_403_FORBIDDEN
            )

        correct_answers = 0

        saved_answers = []

        correct_answers = 0

        # Salva respostas
        for item in answers:

            question = Question.objects.filter(
                id=item["question"],
                topic=topic
            ).first()

            if not question:

                continue

            alternative = Alternative.objects.filter(
                id=item["selected_alternative"],
                question=question
            ).first()

            if not alternative:

                continue

            answer = UserAnswer.objects.create(
                user=request.user,
                question=question,
                selected_alternative=alternative,
                is_correct=alternative.is_correct
            )

            saved_answers.append(answer.id)

            if alternative.is_correct:
                correct_answers += 1

        # Marca tópico como concluído
        UserProgress.objects.update_or_create(
            user=request.user,
            topic=topic,
            defaults={
                "completed": True
            }
        )

        return Response(
            {
                "message": "Quiz submitted successfully",

                "topic_completed": True,

                "correct_answers": correct_answers,

                "total_questions": len(answers),

                "saved_answers": saved_answers
            },
            status=status.HTTP_201_CREATED
        )
