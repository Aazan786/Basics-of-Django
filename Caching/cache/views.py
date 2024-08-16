from django.shortcuts import render
from django.core.cache import cache
# from django.views.decorators.cache import cache_page
# Create your views here.
# @cache_page(600) # it opitional if cache mention on urls
# def home(request):
#     return render(request, "cache/cache.html")


#Low level Api caching
# def home(request):
#     #cache methods
#     mv = cache.get("movie", "has_expired")
#     if mv == 'has_expired':
#         cache.set('movie', 'Gang', 30)
#         cache.get('movie')
#     return render(request, "cache/cache.html",{
#         "fm": mv
#      })

def home(request):
    cache.clear()
    return render(request, "cache/cache.html")