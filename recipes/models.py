from django.db import models

# Create your models here.

class Ingredient(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True, editable=False)
	updated_at = models.DateTimeField(auto_now=True, editable=False)


class Recipe(models.Model):
	id = models.AutoField(primary_key=True)
	yum_id = models.CharField(max_length=255)
	recipeName = models.CharField(max_length=255)
	ingredients = models.TextField()
	cuisines = models.TextField(null=True)
	courses = models.TextField(null=True)
	smallImageUrls = models.CharField(max_length=255, null=True)
	sourceDisplayName = models.CharField(max_length=200)
	used_db_ingredients = models.TextField()


class UsedIn(models.Model):
	recipe_id = models.IntegerField()
	ingredient_id = models.IntegerField()
	recipeName = models.CharField(max_length=255)
	ingredientName = models.CharField(max_length=255)



