from rest_framework import serializers
from .models import Recipe
from membership.serializers import MemberSerializer

class RecipeSerializer(serializers.ModelSerializer):
    created_by = MemberSerializer()
    class Meta:
        model = Recipe
        fields = ['id', 'title', 'ingredients', 'instructions', 'created_by']
        read_only_fields = ['created_by']                                                                                                                