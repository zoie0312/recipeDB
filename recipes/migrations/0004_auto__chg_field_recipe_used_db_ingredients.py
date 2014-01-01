# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Recipe.used_db_ingredients'
        db.alter_column(u'recipes_recipe', 'used_db_ingredients', self.gf('django.db.models.fields.TextField')())

    def backwards(self, orm):

        # Changing field 'Recipe.used_db_ingredients'
        db.alter_column(u'recipes_recipe', 'used_db_ingredients', self.gf('django.db.models.fields.CommaSeparatedIntegerField')(max_length=255))

    models = {
        u'recipes.ingredient': {
            'Meta': {'object_name': 'Ingredient'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'recipes.recipe': {
            'Meta': {'object_name': 'Recipe'},
            'courses': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'cuisines': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ingredients': ('django.db.models.fields.TextField', [], {}),
            'recipeName': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'smallImageUrls': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'sourceDisplayName': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'used_db_ingredients': ('django.db.models.fields.TextField', [], {}),
            'yum_id': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'recipes.usedin': {
            'Meta': {'object_name': 'UsedIn'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ingredientName': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'ingredient_id': ('django.db.models.fields.IntegerField', [], {}),
            'recipeName': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'recipe_id': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['recipes']