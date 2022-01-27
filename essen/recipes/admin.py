from django.contrib import admin

from recipes.models import Recipe, Ingredient

class IngredientInline(admin.TabularInline):
   model = Ingredient
   fields = ('name', 'quantity', 'unit')

class RecipeAdmin(admin.ModelAdmin):
   inlines = [IngredientInline]

admin.site.register(Recipe, RecipeAdmin)