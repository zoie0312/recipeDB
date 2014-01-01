from django.contrib import admin
from .models import Ingredient, Recipe, UsedIn

class IngredientAdmin(admin.ModelAdmin):
	date_hierarchy = "created_at"
	#fields = ("id", "name")
	list_display = ["id", "name"]
	list_display_link = ["name"]
	list_editable = ["name"]
	list_filter = ["name"]
	search_fields = ["name"]

class RecipeAdmin(admin.ModelAdmin):
	#fields = ("id", "yum_id", "recipeName", "ingredients", "cuisines",
	#	"courses", "smallImageUrls", "sourceDisplayName")
	list_display = ["id", "recipeName", "used_db_ingredients", "cuisines", "courses"]
	list_display_link = ["recipeName"]
	list_filter = ["recipeName", "cuisines", "courses"]
	search_fields = ["recipeName", "cuisines", "courses"]

class UsedInAdmin(admin.ModelAdmin):
	#fields = ("recipe_id", "ingredient_id", "recipeName", "ingredientName")
	list_display = ["recipe_id", "ingredient_id", "recipeName", "ingredientName"]
	list_filter = ["ingredientName", "recipeName"]
	search_fields = ["ingredientName"]


admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(UsedIn, UsedInAdmin)


