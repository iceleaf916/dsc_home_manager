#! /usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib import admin

from models import (Album, Software, AlbumPublish)

class SoftwareAdmin(admin.ModelAdmin):
    list_display = ('pkg_name', 'language', 'display_name', 'short_desc')
    list_filter = ('language', )
    search_fields = ('pkg_name', 'display_name')
    list_per_page = 30
        
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('name', 'language', 'last_modified')
    list_filter = ('language', )
    search_fields = ('name', )
    filter_horizontal = ('softwares', )
    date_hierarchy = 'last_modified'

    #def formfield_for_manytomany(self, db_field, request=None, **kwargs):
        #if db_field.name == 'softwares':
            #kwargs['queryset'] = Software.objects.filter(language=request.language)
        #return super(AlbumAdmin, self).formfield_for_manytomany(
            #db_field, request=request, **kwargs)

class AlbumPublishAdmin(admin.ModelAdmin):
    list_display = ('name', 'language', 'pub_datetime', 'status')
    list_filter = ('language', )
    filter_horizontal = ('albums', )
    date_hierarchy = 'pub_datetime'

    #def formfield_for_manytomany(self, db_field, request=None, **kwargs):
        #if db_field.name == 'albums':
            #kwargs['queryset'] = Album.objects.filter(language=request.language)
        #return super(AlbumPublishAdmin, self).formfield_for_manytomany(
            #db_field, request=request, **kwargs)

admin.site.register(Software, SoftwareAdmin)
admin.site.register(Album, AlbumAdmin)
admin.site.register(AlbumPublish, AlbumPublishAdmin)

