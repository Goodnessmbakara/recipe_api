from django.db import models

class Recipe(models.Model):
    title = models.CharField(max_length=100)
    ingredients = models.TextField()
    instructions = models.TextField()
    created_by = models.ForeignKey('membership.Member', on_delete = models.CASCADE,  related_name='recipes')
    
    def __str__(self):
        return self.title