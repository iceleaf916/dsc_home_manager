# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'AlbumPublic'
        db.delete_table(u'album_albumpublic')

        # Removing M2M table for field albums on 'AlbumPublic'
        db.delete_table(db.shorten_name(u'album_albumpublic_albums'))

        # Adding model 'AlbumPublish'
        db.create_table(u'album_albumpublish', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('language', self.gf('django.db.models.fields.CharField')(default='en_us', max_length=25)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('status', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'album', ['AlbumPublish'])

        # Adding M2M table for field albums on 'AlbumPublish'
        m2m_table_name = db.shorten_name(u'album_albumpublish_albums')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('albumpublish', models.ForeignKey(orm[u'album.albumpublish'], null=False)),
            ('album', models.ForeignKey(orm[u'album.album'], null=False))
        ))
        db.create_unique(m2m_table_name, ['albumpublish_id', 'album_id'])


    def backwards(self, orm):
        # Adding model 'AlbumPublic'
        db.create_table(u'album_albumpublic', (
            ('status', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('language', self.gf('django.db.models.fields.CharField')(default='en_us', max_length=25)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, auto_now_add=True, blank=True)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'album', ['AlbumPublic'])

        # Adding M2M table for field albums on 'AlbumPublic'
        m2m_table_name = db.shorten_name(u'album_albumpublic_albums')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('albumpublic', models.ForeignKey(orm[u'album.albumpublic'], null=False)),
            ('album', models.ForeignKey(orm[u'album.album'], null=False))
        ))
        db.create_unique(m2m_table_name, ['albumpublic_id', 'album_id'])

        # Deleting model 'AlbumPublish'
        db.delete_table(u'album_albumpublish')

        # Removing M2M table for field albums on 'AlbumPublish'
        db.delete_table(db.shorten_name(u'album_albumpublish_albums'))


    models = {
        u'album.album': {
            'Meta': {'object_name': 'Album'},
            'cover_pic': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'default': "'en_us'", 'max_length': '25'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'order': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'softwares': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['album.Software']", 'symmetrical': 'False', 'blank': 'True'}),
            'summary': ('django.db.models.fields.TextField', [], {'max_length': '2550'})
        },
        u'album.albumpublish': {
            'Meta': {'ordering': "['-created']", 'object_name': 'AlbumPublish'},
            'albums': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['album.Album']", 'symmetrical': 'False', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'default': "'en_us'", 'max_length': '25'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '1'})
        },
        u'album.software': {
            'Meta': {'object_name': 'Software'},
            'display_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'default': "'en_us'", 'max_length': '25'}),
            'long_desc': ('django.db.models.fields.TextField', [], {'max_length': '2550'}),
            'order': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'pkg_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'short_desc': ('django.db.models.fields.CharField', [], {'max_length': '2550'}),
            'software_pic': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['album']