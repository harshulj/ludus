# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Faculty.salutation'
        db.add_column('courses_faculty', 'salutation',
                      self.gf('django.db.models.fields.CharField')(default='Dr', max_length=4),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Faculty.salutation'
        db.delete_column('courses_faculty', 'salutation')


    models = {
        'courses.course': {
            'Meta': {'object_name': 'Course'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '60'})
        },
        'courses.faculty': {
            'Meta': {'object_name': 'Faculty'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'courses': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'faculties'", 'symmetrical': 'False', 'to': "orm['courses.Course']"}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'salutation': ('django.db.models.fields.CharField', [], {'default': "'Dr'", 'max_length': '4'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['courses']