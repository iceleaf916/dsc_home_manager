# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Software'
        db.create_table(u'album_software', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('pkg_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('language', self.gf('django.db.models.fields.CharField')(default='en_us', max_length=25)),
            ('display_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('short_desc', self.gf('django.db.models.fields.CharField')(max_length=2550)),
            ('long_desc', self.gf('django.db.models.fields.TextField')(max_length=2550)),
            ('software_pic', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
            ('order', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'album', ['Software'])

        # Adding model 'Album'
        db.create_table(u'album_album', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('language', self.gf('django.db.models.fields.CharField')(default='en_us', max_length=25)),
            ('summary', self.gf('django.db.models.fields.TextField')(max_length=2550)),
            ('cover_pic', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
            ('order', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('last_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'album', ['Album'])

        # Adding M2M table for field softwares on 'Album'
        m2m_table_name = db.shorten_name(u'album_album_softwares')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('album', models.ForeignKey(orm[u'album.album'], null=False)),
            ('software', models.ForeignKey(orm[u'album.software'], null=False))
        ))
        db.create_unique(m2m_table_name, ['album_id', 'software_id'])

        # Adding model 'AlbumPublish'
        db.create_table(u'album_albumpublish', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('language', self.gf('django.db.models.fields.CharField')(default='en_us', max_length=25)),
            ('status', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('pub_datetime', self.gf('django.db.models.fields.DateTimeField')()),
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
        # Deleting model 'Software'
        db.delete_table(u'album_software')

        # Deleting model 'Album'
        db.delete_table(u'album_album')

        # Removing M2M table for field softwares on 'Album'
        db.delete_table(db.shorten_name(u'album_album_softwares'))

        # Deleting model 'AlbumPublish'
        db.delete_table(u'album_albumpublish')

        # Removing M2M table for field albums on 'AlbumPublish'
        db.delete_table(db.shorten_name(u'album_albumpublish_albums'))


    models = {
        u'album.album': {
            'Meta': {'object_name': 'Album'},
            'cover_pic': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'default': "'en_us'", 'max_length': '25'}),
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
            'language': ('django.db.models.fields.CharField', [], {'default': "'en_us'", 'max_length': '25'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'pub_datetime': ('django.db.models.fields.DateTimeField', [], {}),
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
            'software_pic': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'})
        }
    }

    complete_apps = ['album']