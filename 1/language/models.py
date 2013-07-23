#! /usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models

# Create your models here.
class Language(models.Model):
    lang_code = models.CharField(max_length=255, unique=True, verbose_name="语言代码")
    
    def __unicode__(self):
        return self.lang_code
