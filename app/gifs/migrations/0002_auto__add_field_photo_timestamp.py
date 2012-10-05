# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Photo.timestamp'
        db.add_column('gifs_photo', 'timestamp',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

    def backwards(self, orm):
        # Deleting field 'Photo.timestamp'
        db.delete_column('gifs_photo', 'timestamp')

    models = {
        'gifs.photo': {
            'Meta': {'object_name': 'Photo'},
            'date_downloaded': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_posted': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'height': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'note_count': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'post_url': ('django.db.models.fields.URLField', [], {'unique': 'True', 'max_length': '255'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'photos'", 'symmetrical': 'False', 'to': "orm['gifs.Tag']"}),
            'tags_json': ('jsonfield.fields.JSONField', [], {'null': 'True', 'blank': 'True'}),
            'timestamp': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '255'}),
            'width': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'gifs.tag': {
            'Meta': {'object_name': 'Tag'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'})
        }
    }

    complete_apps = ['gifs']