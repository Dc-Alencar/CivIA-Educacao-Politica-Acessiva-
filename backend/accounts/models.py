from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
	accepted_terms = models.BooleanField(
		default=False,
		help_text='Regista se o utilizador aceitou os Termos de Uso Cívico no primeiro acesso (RN13).',
	)
	terms_accepted_at = models.DateTimeField(
		null=True,
		blank=True,
		help_text='Data e hora do consentimento para auditoria da LGPD.',
	)

