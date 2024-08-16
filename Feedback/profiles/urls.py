from django.urls import path
from .views import*

app_name = "profiles"
urlpatterns = [
    path("profile", CreateProfile.as_view()),
    path("list", ProfileView.as_view())
]