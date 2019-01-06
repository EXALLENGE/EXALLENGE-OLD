from django.urls import path, include
from django.contrib import admin

admin.autodiscover()

urlpatterns = [
    path("", include('hello.urls')),
    path("admin/", admin.site.urls),
]
