# The `urlpatterns` list routes URLs to views. For more information please see:
#     https://docs.djangoproject.com/en/4.1/topics/http/urls/

from django.contrib import admin
from django.urls import path, include

urlpatterns = (
    path("admin/", admin.site.urls),
    path("album/", include("music.my_album.urls")),
    path("profile/", include("music.my_profile.urls")),
)
