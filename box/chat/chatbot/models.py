

# Create your models here.
from django.db import models

class Conversation(models.Model):
    user_input = models.CharField(max_length=255)
    bot_response = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return f'{self.user_input} - {self.bot_response}'