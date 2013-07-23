# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Software.language'
        db.delete_column(u'album_software', 'language')

        # Deleting field 'AlbumPublish.language'
        db.delete_column(u'album_albumpublish', 'language')

        # Deleting field 'Album.language'
        db.delete_column(u'album_album', 'language')


    def backwards(self, orm):
        # Adding field 'Software.language'
        db.add_column(u'album_software', 'language',
                      self.gf('django.db.models.fields.CharField')(default='en_us', max_length=25),
                      keep_default=False)

        # Adding field 'AlbumPublish.language'
        db.add_column(u'album_albumpublish', 'language',
                      self.gf('django.db.models.fields.CharField')(default='en_us', max_length=25),
                      keep_default=False)

        # Adding field 'Album.language'
        db.add_column(u'album_album', 'language',
                      self.gf('django.db.models.fields.CharField')(default='en_us', max_length=25),
                      keep_default=False)


    models = {
        u'album.album': {
            'Meta': {'object_name': 'Album'},
            'cover_pic': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language_code': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['language.Language']"}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'order': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'softwares': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['album.Software']", 'symmetrical': 'False', 'blank': 'True'}),
            'summary': ('django.db.models.fields.TextField', [], {'max_length': '2550'})
        },
        u'album.albumpublish': {
            'Meta': {'ordering': "['-pub_datetime']", 'object_name': 'AlbumPublish'},
            'albums': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['album.Album']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language_code': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['language.Language']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'pub_datetime': ('django.db.models.fields.DateTimeField', [], {}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '1'})
        },
        u'album.software': {
            'Meta': {'object_name': 'Software'},
            'display_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language_code': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['language.Language']"}),
            'long_desc': ('django.db.models.fields.TextField', [], {'max_length': '2550'}),
            'order': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'pkg_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'short_desc': ('django.db.models.fields.CharField', [], {'max_length': '2550'}),
            'software_pic': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'})
        },
        u'language.language': {
            'Meta': {'object_name': 'Language'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lang_code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        }
    }

    complete_apps = ['album']