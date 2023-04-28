from django.contrib import admin
from django.urls import path, include
from polls import views

urlpatterns = [
    path("generate_teachers/", include(views.teachers)),
    path("admin/", admin.site.urls),
]
