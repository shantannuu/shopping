from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="SHOPHOME"),
    path("Post/<int:id>", views.Post, name="Posthere")

]
