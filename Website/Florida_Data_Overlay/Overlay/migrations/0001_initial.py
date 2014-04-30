# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Births'
        db.create_table(u'Overlay_births', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('year', self.gf('django.db.models.fields.IntegerField')()),
            ('county', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('mothersAge', self.gf('django.db.models.fields.IntegerField')()),
            ('mothersEdu', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('source', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('isRepeat', self.gf('django.db.models.fields.BooleanField')()),
            ('births', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'Overlay', ['Births'])

        # Adding model 'Diseases'
        db.create_table(u'Overlay_diseases', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('year', self.gf('django.db.models.fields.IntegerField')()),
            ('county', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('topic', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('source', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('count', self.gf('django.db.models.fields.IntegerField')()),
            ('rate', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal(u'Overlay', ['Diseases'])


    def backwards(self, orm):
        # Deleting model 'Births'
        db.delete_table(u'Overlay_births')

        # Deleting model 'Diseases'
        db.delete_table(u'Overlay_diseases')


    models = {
        u'Overlay.births': {
            'Meta': {'object_name': 'Births'},
            'births': ('django.db.models.fields.IntegerField', [], {}),
            'county': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'isRepeat': ('django.db.models.fields.BooleanField', [], {}),
            'mothersAge': ('django.db.models.fields.IntegerField', [], {}),
            'mothersEdu': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'source': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        u'Overlay.diseases': {
            'Meta': {'object_name': 'Diseases'},
            'count': ('django.db.models.fields.IntegerField', [], {}),
            'county': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'rate': ('django.db.models.fields.FloatField', [], {}),
            'source': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'topic': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['Overlay']