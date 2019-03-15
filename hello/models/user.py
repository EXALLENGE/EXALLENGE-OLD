from django.db import models


class User(models.Model):
    name = models.CharField(max_length=120)
    login = models.CharField(max_length=120)
    psw = models.CharField(max_length=88)
    tmp_url = models.CharField(max_length=25)
    logged_in_cookie = models.CharField(max_length=120)
