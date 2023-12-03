from django.shortcuts import render
from utils.recipes.factory import make_recipe

from recipes.models import Recipe


def home(request):
    recipes = Recipe.objects.filter(
        is_published=True
    ).order_by('-id')
    
    return render(request, 'recipes/pages/home.html', context={
        'recipes': recipes,
    })

def category(request, category_id):
    recipes = Recipe.objects.filter(
        category__id=category_id,
        is_published=True
    ).order_by('-id')
    
    return render(request, 'recipes/pages/category.html', context={
        'recipes': recipes,
    })
    

def recipe(request, id):
    recipe = Recipe.objects.filter(
        id=id,
        is_published=True
        ).order_by('-id').first()
    
    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipe': recipe,
        'is_detail_page': True,
    })
    