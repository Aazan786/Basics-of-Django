from django.urls import path

from .views import*

app_name = "cookies"
urlpatterns = [
    path("set", set_cookies),
    path("get", get_cookies),
    path("del", del_cookies),

]
