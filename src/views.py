from rest_framework import generics
from .models import Recipe
from .serializers import RecipeSerializer

class RecipeListCreate(generics.ListCreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class RecipeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer