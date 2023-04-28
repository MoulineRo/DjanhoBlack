from django.contrib import admin
from django.urls import path

from polls import views

urlpatterns = [
    path("", views.index),
    path("generate_teachers/", views.teachers),
    path("admin/", admin.site.urls),
]
