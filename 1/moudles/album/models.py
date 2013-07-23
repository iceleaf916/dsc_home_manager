#! /usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
from language.models import Language

ALBUM_COVER_PIC_PATH = "album_pictures/cover"
ALBUM_SOFTWARE_PIC_PATH = "album_pictures/software"

class Software(models.Model):
    pkg_name = models.CharField(max_length=255, verbose_name='包名')
    language_code = models.ForeignKey(Language, verbose_name=u"语言")
    display_name = models.CharField(max_length=255, verbose_name='显示名称')
    short_desc = models.CharField(max_length=2550, verbose_name='一句话描述')
    long_desc = models.TextField(max_length=2550, verbose_name='推荐简介')
    software_pic = models.ImageField(upload_to=ALBUM_SOFTWARE_PIC_PATH, verbose_name="软件宣传图片", blank=True)
    order = models.IntegerField(blank=True, null=True, verbose_name="排序")

    def __unicode__(self):
        return "[%s]%s" % (self.language_code, self.pkg_name)

    class Meta:
        verbose_name = "推荐软件"
        verbose_name_plural = "推荐软件"

class Album(models.Model):
    name = models.CharField(max_length=255, verbose_name="专辑名称")
    language_code = models.ForeignKey(Language, verbose_name=u"语言")
    summary = models.TextField(max_length=2550, verbose_name="专辑简介")
    cover_pic = models.ImageField(upload_to=ALBUM_COVER_PIC_PATH, verbose_name="专辑封面", blank=True)
    order = models.IntegerField(blank=True, null=True, verbose_name="排序")
    last_modified = models.DateTimeField(auto_now_add=True, verbose_name="发布时间")

    softwares = models.ManyToManyField(Software, verbose_name=u"软件列表", blank=True)

    def __unicode__(self):
        return "[%s]%s" % (self.language_code, self.name)

    class Meta:
        verbose_name = "推荐专辑"
        verbose_name_plural = "推荐专辑"

class AlbumPublish(models.Model):
    STATUS_CHOICE = (
        (1, "编辑"),
        (2, "测试"),
        (3, "发布"),
        (4, "存档"),
        )
    name = models.CharField(max_length=255, verbose_name="发布名称")
    language_code = models.ForeignKey(Language, verbose_name=u"语言")
    status = models.IntegerField(choices=STATUS_CHOICE, default=1, verbose_name="状态")
    pub_datetime = models.DateTimeField(verbose_name="发布时间")

    albums = models.ManyToManyField(Album, verbose_name=u"要发布的专辑", blank=True)

    def __unicode__(self):
        return "[%s]%s" % (self.language_code, self.name)

    class Meta:
        verbose_name = "发布管理"
        verbose_name_plural = "发布管理"
        ordering = ['-pub_datetime'] 

    @property
    def is_test(self):
        return self.status == 2

    @property
    def is_public(self):
        return self.status == 3
