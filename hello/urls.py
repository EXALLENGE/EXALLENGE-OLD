from django.urls import path
from django.contrib import admin

from .views import index, login, courses

admin.autodiscover()

urlpatterns = [
    path("", index, name="index"),
    path("login", login, name="login"),
    path("courses", courses, name="courses")
]
