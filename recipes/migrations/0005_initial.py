# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Ingredient'
        db.create_table(u'recipes_ingredient', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'recipes', ['Ingredient'])

        # Adding model 'Recipe'
        db.create_table(u'recipes_recipe', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('yum_id', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('recipeName', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('ingredients', self.gf('django.db.models.fields.TextField')()),
            ('cuisines', self.gf('django.db.models.fields.TextField')(null=True)),
            ('courses', self.gf('django.db.models.fields.TextField')(null=True)),
            ('smallImageUrls', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('sourceDisplayName', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('used_db_ingredients', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'recipes', ['Recipe'])

        # Adding model 'UsedIn'
        db.create_table(u'recipes_usedin', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('recipe_id', self.gf('django.db.models.fields.IntegerField')()),
            ('ingredient_id', self.gf('django.db.models.fields.IntegerField')()),
            ('recipeName', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('ingredientName', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'recipes', ['UsedIn'])


    def backwards(self, orm):
        # Deleting model 'Ingredient'
        db.delete_table(u'recipes_ingredient')

        # Deleting model 'Recipe'
        db.delete_table(u'recipes_recipe')

        # Deleting model 'UsedIn'
        db.delete_table(u'recipes_usedin')


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