from django.db.models import Q
from django.http.response import Http404
from django.shortcuts import render

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


def search(request):
    search_term = request.GET.get('search', '').strip()

    if not search_term:
        raise Http404()

    recipes = Recipe.objects.filter(
        Q(title__icontains=search_term) | 
        Q(description__icontains=search_term) # verificar uma receita cujo título ou descrição contenha o valor de search_term
    ).order_by('-id')
        
    return render(request, 'recipes/pages/search.html', context={
        'page_title': f'Search for "{search_term}" |',
        'recipes': recipes,
    })
    