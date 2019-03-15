from django.urls import path
from django.contrib import admin

from .views import index, login, courses, registration, profile, check_registration

admin.autodiscover()

urlpatterns = [
    path("", index, name="index"),
    path("login", login, name="login"),
    path("registration", registration, name="registration"),
    path("check_registration/<unique_hash>", check_registration, name="check_registration"),
    path("profile", profile, name="profile"),
    path("courses", courses, name="courses")
]
