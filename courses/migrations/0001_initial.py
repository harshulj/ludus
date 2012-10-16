# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Course'
        db.create_table('courses_course', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=60)),
        ))
        db.send_create_signal('courses', ['Course'])

        # Adding model 'Faculty'
        db.create_table('courses_faculty', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
        ))
        db.send_create_signal('courses', ['Faculty'])

        # Adding M2M table for field courses on 'Faculty'
        db.create_table('courses_faculty_courses', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('faculty', models.ForeignKey(orm['courses.faculty'], null=False)),
            ('course', models.ForeignKey(orm['courses.course'], null=False))
        ))
        db.create_unique('courses_faculty_courses', ['faculty_id', 'course_id'])


    def backwards(self, orm):
        # Deleting model 'Course'
        db.delete_table('courses_course')

        # Deleting model 'Faculty'
        db.delete_table('courses_faculty')

        # Removing M2M table for field courses on 'Faculty'
        db.delete_table('courses_faculty_courses')


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
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['courses']