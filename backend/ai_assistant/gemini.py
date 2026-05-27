from google.genai import Client

from django.conf import settings

client = Client(
    api_key=settings.GEMINI_API_KEY
)
