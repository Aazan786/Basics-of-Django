from django.urls import path
from .views import*

app_name = "enroll"
urlpatterns = [
    path("", showformdata),
    path("success", thankyou)
]