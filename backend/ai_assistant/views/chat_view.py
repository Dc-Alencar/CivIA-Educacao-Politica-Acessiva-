from rest_framework.views import APIView

from rest_framework.response import Response

from rest_framework.permissions import (
    IsAuthenticated
)

from rest_framework import status

from ai_assistant.serializers import (
    ChatSerializer
)

from ai_assistant.utils.load_knowledge import (
    load_all_knowledge
)

from ai_assistant.gemini import client

from content.models import Topic

class ChatView(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request):


            message = request.data.get(
                "message"
            )

            knowledge = load_all_knowledge()

            prompt = f"""
                Você é um assistente educacional.

                Seu foco é ensinar:
                - cidadania
                - direitos fundamentais
                - Constituição Federal de 1988
                - direitos básicos

                Utilize prioritariamente o conteúdo abaixo:

                {knowledge}

                Pergunta do usuário:

                {message}
                """
            
            response = client.models.generate_content(

                model="gemini-2.5-flash",

                contents=prompt
            )

            return Response(

                {
                    "response": response.text
                },

                status=status.HTTP_200_OK
            )