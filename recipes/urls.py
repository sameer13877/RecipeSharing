# recipes/urls.py
from django.urls import path
from .views import RecipeListView, RecipeDetailView, RecipeCreateView, RecipeUpdateView

urlpatterns = [
    path('', RecipeListView.as_view(), name='recipe_list'),
    path('recipe/<int:pk>/', RecipeDetailView.as_view(), name='recipe_detail'),
    path('recipes/create/', RecipeCreateView.as_view(), name='create_recipe'),
    path('recipes/<int:pk>/update/', RecipeUpdateView.as_view(), name='update_recipe'),
]
