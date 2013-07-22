#! /usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib import admin

from models import (Album, Software, AlbumPublic)

class SoftwareAdmin(admin.ModelAdmin):
    list_display = ('pkg_name', 'language', 'display_name', 'short_desc')
    list_filter = ('language', )
    search_fields = ('pkg_name', 'display_name')
    list_per_page = 20
        
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('name', 'language', 'summary')
    list_filter = ('language', )
    filter_horizontal = ('softwares', )

    def formfield_for_manytomany(self, db_field, request=None, **kwargs):
        if db_field.name == 'softwares':
            kwargs['queryset'] = Software.objects.filter(language=request.language)
        return super(AlbumAdmin, self).formfield_for_manytomany(
            db_field, request=request, **kwargs)

class AlbumPublicAdmin(admin.ModelAdmin):
    list_display = ('name', 'language', 'created', 'status')
    list_filter = ('language', )
    filter_horizontal = ('albums', )

    def formfield_for_manytomany(self, db_field, request=None, **kwargs):
        if db_field.name == 'albums':
            kwargs['queryset'] = Album.objects.filter(language=request.language)
        return super(AlbumPublicAdmin, self).formfield_for_manytomany(
            db_field, request=request, **kwargs)

admin.site.register(Software, SoftwareAdmin)
admin.site.register(Album, AlbumAdmin)
admin.site.register(AlbumPublic, AlbumPublicAdmin)

