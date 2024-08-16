from django.urls import path
from .views import*

app_name = "signup"
urlpatterns = [
    path("", signup, name= "sign_up"),
    path("login", user_login, name = "userlogin"),
    path("profile", user_profile, name = "profile"),
    path("logout", user_logout, name = "logout"),
    path("change_password", change_password, name = "change_password"),
    path("userdetail/<int:id>", user_detail, name = "userdetail")
]
