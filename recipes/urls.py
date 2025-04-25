# recipes/urls.py
from django.urls import path
from .views import (
    RecipeListAPIView, 
    RecipeDetailAPIView, 
    RatingCreateAPIView,
    CommentCreateAPIView, 
    RecipeCollectionCreateAPIView)
from .views import hello_world

urlpatterns = [
    path("recipes/", RecipeListAPIView.as_view(), name="recipe-list"),
    path("recipes/<int:pk>/", RecipeDetailAPIView.as_view(), name="recipe-detail"),
    path("recipes/<int:pk>/rate/", RatingCreateAPIView.as_view(), name="rate-recipe"),
    path("recipes/<int:pk>/comment/", CommentCreateAPIView.as_view(), name="comment-recipe"),
    path("recipe-collections/create/", RecipeCollectionCreateAPIView.as_view(), name="create-recipe-collection"),
    path("hello/", hello_world, name="hello-world"),
]
