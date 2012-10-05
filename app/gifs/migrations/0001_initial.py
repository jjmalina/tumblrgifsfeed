# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Tag'
        db.create_table('gifs_tag', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
        ))
        db.send_create_signal('gifs', ['Tag'])

        # Adding model 'Photo'
        db.create_table('gifs_photo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('post_url', self.gf('django.db.models.fields.URLField')(unique=True, max_length=255)),
            ('note_count', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=255)),
            ('height', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('width', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('tags_json', self.gf('jsonfield.fields.JSONField')(null=True, blank=True)),
            ('date_posted', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('date_downloaded', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('gifs', ['Photo'])

        # Adding M2M table for field tags on 'Photo'
        db.create_table('gifs_photo_tags', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('photo', models.ForeignKey(orm['gifs.photo'], null=False)),
            ('tag', models.ForeignKey(orm['gifs.tag'], null=False))
        ))
        db.create_unique('gifs_photo_tags', ['photo_id', 'tag_id'])

    def backwards(self, orm):
        # Deleting model 'Tag'
        db.delete_table('gifs_tag')

        # Deleting model 'Photo'
        db.delete_table('gifs_photo')

        # Removing M2M table for field tags on 'Photo'
        db.delete_table('gifs_photo_tags')

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