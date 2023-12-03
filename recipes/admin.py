from django.contrib import admin
from .models import Category, Recipe

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    ...

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    ...
