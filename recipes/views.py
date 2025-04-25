from .models import Recipe, Comment, Rating, RecipeCollection
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import RecipeSerializer, RatingSerializer, CommentSerializer
from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated
from recipes import models
from rest_framework.decorators import api_view

class RecipeListAPIView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):
        recipes = Recipe.objects.all()
        serializer = RecipeSerializer(recipes,many= True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = RecipeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class RecipeDetailAPIView(APIView):

    permission_classes = [IsAuthenticated]
    
    def get(self, request, pk):
    
        try:
            recipe = Recipe.objects.get(pk=pk)
            comments = Comment.objects.filter(recipe=recipe).values()
            ratings = Rating.objects.filter(recipe=recipe)
            avg_rating = ratings.aggregate(models.Avg('rating'))['rating__avg'] or 0

            data = {
                    "recipes" : RecipeSerializer(recipe).data,
                    'comments': CommentSerializer(comments, many=True).data,
                    'ratings' : RatingSerializer(ratings,many=True).data,
                    'avg_rating' : avg_rating
            }
            return Response(data)
        except Recipe.DoesNotExist:
            return Response({"Error":"Recipe does not Exist"},status= 400)
    
    def put(self, request, pk): 
        try:
            recipe = Recipe.objects.get(pk=pk)
        except Recipe.DoesNotExist:
            return Response({"Error": "Recipe does not exist"}, status=status.HTTP_404_NOT_FOUND)

        serializer = RecipeSerializer(recipe, data=request.data) 
        if serializer.is_valid(): 
            serializer.save() 
            return Response(serializer.data) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    
    def delete(self, request, pk):
        try:
            recipe = Recipe.objects.get(pk=pk)
        except Recipe.DoesNotExist:
            return Response({"Error": "Recipe does not exist"}, status=status.HTTP_400_BAD_REQUEST)
        recipe.delete()
        return Response({"Success": "Recipe deleted successfully"},status=status.HTTP_204_NO_CONTENT)
    
class RatingCreateAPIView(APIView):


    def post(self, request, pk ):
        try:
            recipe= Recipe.objects.get(pk=pk)
        except Recipe.DoesNotExist:
            return Response({"Errof":"Recipe does not exist"}, status=204)
        
        serializer = RatingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user, recipe=recipe)
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
class CommentCreateAPIView(APIView):

    permission_classes = [IsAuthenticated]

    def post(self,request, pk):
        try:
           recipe = Recipe.objects.get(pk=pk)
        except Recipe.DoesNotExist:
            return Response({"Error":"Recipe Does not Exist"}, status=204)
        
        serializer= CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user, recipe=recipe)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({"Error":"Recipe does not Exist"}, status=204)
    

class RecipeCollectionCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        pass


@api_view()
def hello_world(request):
    return Response({"message": "Hello, world!"})
