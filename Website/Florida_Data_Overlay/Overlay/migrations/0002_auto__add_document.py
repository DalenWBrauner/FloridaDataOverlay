# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Document'
        db.create_table(u'Overlay_document', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('docfile', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
        ))
        db.send_create_signal(u'Overlay', ['Document'])


    def backwards(self, orm):
        # Deleting model 'Document'
        db.delete_table(u'Overlay_document')


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
        },
        u'Overlay.document': {
            'Meta': {'object_name': 'Document'},
            'docfile': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['Overlay']