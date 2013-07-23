#! /usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib import admin

from models import (Album, Software, AlbumPublish)

class SoftwareAdmin(admin.ModelAdmin):
    list_display = ('pkg_name', 'language_code', 'display_name', 'short_desc', 'order')
    list_filter = ('language_code', )
    search_fields = ('pkg_name', 'display_name')
    list_per_page = 30
    list_editable = ('display_name', 'order', )
        
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('name', 'language_code', 'last_modified', 'order')
    list_filter = ('language_code', )
    search_fields = ('name', )
    filter_horizontal = ('softwares', )
    date_hierarchy = 'last_modified'
    list_editable = ('order', )

    #def formfield_for_manytomany(self, db_field, request=None, **kwargs):
        #if db_field.name == 'softwares':
            #kwargs['queryset'] = Software.objects.filter(language_code=request.language_code)
        #return super(AlbumAdmin, self).formfield_for_manytomany(
            #db_field, request=request, **kwargs)

class AlbumPublishAdmin(admin.ModelAdmin):
    list_display = ('name', 'language_code', 'pub_datetime', 'status')
    list_filter = ('language_code', )
    filter_horizontal = ('albums', )
    date_hierarchy = 'pub_datetime'

    #def formfield_for_manytomany(self, db_field, request=None, **kwargs):
        #if db_field.name == 'albums':
            #kwargs['queryset'] = Album.objects.filter(language_code=request.language_code)
        #return super(AlbumPublishAdmin, self).formfield_for_manytomany(
            #db_field, request=request, **kwargs)

admin.site.register(Software, SoftwareAdmin)
admin.site.register(Album, AlbumAdmin)
admin.site.register(AlbumPublish, AlbumPublishAdmin)

