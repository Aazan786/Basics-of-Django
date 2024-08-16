from django.shortcuts import render
from .models import Recipe

# Create your views here.
def recipes_view(request):
    recipes = Recipe.objects.all()
    return render(request, 'app/recipes.html', {
        'recipes': recipes
    })

# Low level cache
from django.core.cache import cache

def cache_recipes_view(request):
    recipes = cache.get('recipes')
    if recipes is None:
        recipes = Recipe.objects.all()
        cache.set('recipes', recipes)

    return render(request, 'app/recipes.html', {
        'recipes': recipes
    })