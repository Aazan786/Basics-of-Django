from django.urls import path
from django.contrib import admin
from .views import*

app_name = "book_outlet"
urlpatterns = [
    path("", index),
    path("<slug:slug>", book_details,  name="book_details"),
]
