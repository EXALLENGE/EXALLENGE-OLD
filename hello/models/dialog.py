from django.db import models

from .course import Course


class Dialog(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    pass