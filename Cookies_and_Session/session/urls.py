from django.urls import path
from .views import*

app_name = "session"
urlpatterns = [
    path("setsession", set_session),
    path("getsession", get_session),
    path("delsession", del_session),

]
