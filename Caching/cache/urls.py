from django.urls import path
# from django.views.decorators.cache import cache_page
from .views import home

app_name = "cache"
urlpatterns = [
#    path("", cache_page(600)(home)),
path("", home)
]
