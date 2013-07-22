#! /usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
from dsc_home_manager.settings import LANGUAGE_CHOICE

ALBUM_COVER_PIC_PATH = "album_pictures/cover"
ALBUM_SOFTWARE_PIC_PATH = "album_pictures/software"

class Software(models.Model):
    pkg_name = models.CharField(max_length=255, verbose_name='包名')
    language = models.CharField(max_length=25, choices=LANGUAGE_CHOICE, default='en_us', verbose_name="语言")
    display_name = models.CharField(max_length=255, verbose_name='显示名称')
    short_desc = models.CharField(max_length=2550, verbose_name='一句话描述')
    long_desc = models.TextField(max_length=2550, verbose_name='推荐简介')
    software_pic = models.ImageField(upload_to=ALBUM_SOFTWARE_PIC_PATH, verbose_name="软件宣传图片")
    order = models.IntegerField(blank=True, null=True, verbose_name="排序")

    def __unicode__(self):
        return "[%s]%s" % (self.language, self.pkg_name)

    class Meta:
        verbose_name = "推荐软件"
        verbose_name_plural = "推荐软件"

class Album(models.Model):
    language = models.CharField(max_length=25, choices=LANGUAGE_CHOICE, default='en_us', verbose_name="语言")
    name = models.CharField(max_length=255, verbose_name="专辑名称")
    summary = models.TextField(max_length=2550, verbose_name="专辑简介")
    cover_pic = models.ImageField(upload_to=ALBUM_COVER_PIC_PATH, verbose_name="专辑封面")
    order = models.IntegerField(blank=True, null=True, verbose_name="排序")

    softwares = models.ManyToManyField(Software, verbose_name=u"软件列表", blank=True)

    def __unicode__(self):
        return "[%s]%s" % (self.language, self.name)

    class Meta:
        verbose_name = "推荐专辑"
        verbose_name_plural = "推荐专辑"

class AlbumPublic(models.Model):
    STATUS_CHOICE = (
        (1, "编辑"),
        (2, "测试"),
        (3, "发布"),
        (4, "存档"),
        )
    language = models.CharField(max_length=25, choices=LANGUAGE_CHOICE, default='en_us', verbose_name="语言")
    name = models.CharField(max_length=255, verbose_name="发布名称")
    status = models.IntegerField(choices=STATUS_CHOICE, default=1, verbose_name="状态")
    created = models.DateTimeField(auto_now=True, auto_now_add=True)

    albums = models.ManyToManyField(Album, verbose_name=u"要发布的专辑", blank=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = "发布管理"
        verbose_name_plural = "发布管理"
        ordering = ['-created'] 

    @property
    def is_test(self):
        return self.status == 2

    @property
    def is_public(self):
        return self.status == 3
