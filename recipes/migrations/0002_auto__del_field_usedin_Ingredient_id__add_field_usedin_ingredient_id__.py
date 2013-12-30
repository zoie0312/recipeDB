# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'UsedIn.Ingredient_id'
        db.delete_column(u'recipes_usedin', 'Ingredient_id')

        # Adding field 'UsedIn.ingredient_id'
        db.add_column(u'recipes_usedin', 'ingredient_id',
                      self.gf('django.db.models.fields.IntegerField')(default=99999),
                      keep_default=False)

        # Adding field 'UsedIn.recipeName'
        db.add_column(u'recipes_usedin', 'recipeName',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255),
                      keep_default=False)

        # Adding field 'UsedIn.ingredientName'
        db.add_column(u'recipes_usedin', 'ingredientName',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'UsedIn.Ingredient_id'
        db.add_column(u'recipes_usedin', 'Ingredient_id',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Deleting field 'UsedIn.ingredient_id'
        db.delete_column(u'recipes_usedin', 'ingredient_id')

        # Deleting field 'UsedIn.recipeName'
        db.delete_column(u'recipes_usedin', 'recipeName')

        # Deleting field 'UsedIn.ingredientName'
        db.delete_column(u'recipes_usedin', 'ingredientName')


    models = {
        u'recipes.ingredient': {
            'Meta': {'object_name': 'Ingredient'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'recipes.recipe': {
            'Meta': {'object_name': 'Recipe'},
            'courses': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'cuisines': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ingredients': ('django.db.models.fields.TextField', [], {}),
            'recipeName': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'smallImageUrls': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'sourceDisplayName': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
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