from django.db import models

from .dialog import Dialog


class Message(models.Model):
    # every message is lesson
    text = models.CharField(max_length=120)
    dialog = models.ForeignKey(Dialog, on_delete=models.CASCADE)
