from django.db import models


class Course(models.Model):
    title = models.CharField(max_length=120)
    description = models.CharField(max_length=1200)
    # False - в разработке, True - готов
    state = models.BooleanField(default=False)
    online = models.BooleanField(default=False)
    offline = models.BooleanField(default=True)
