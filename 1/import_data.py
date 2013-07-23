#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dsc_home_manager.settings")

from deepin_utils.file import get_parent_dir
from moudles.album.models import Software, Album, AlbumPublish
from language.models import Language

def alter_language():
    for s in Software.objects.all():
        cur_lang = Language.objects.filter(lang_code = s.language)
        if len(cur_lang) > 0:
            s.language_code = cur_lang[0]
            s.save()

    for s in Album.objects.all():
        cur_lang = Language.objects.filter(lang_code = s.language)
        if len(cur_lang) > 0:
            s.language_code = cur_lang[0]
            s.save()
        print s.language_code

    for s in AlbumPublish.objects.all():
        cur_lang = Language.objects.filter(lang_code = s.language)
        if len(cur_lang) > 0:
            s.language_code = cur_lang[0]
            s.save()
        print s.language_code

def append_picture():
    #for s in Software.objects.all():
        #jpg_name = s.pkg_name + "_" + s.language_code.lang_code + ".jpg"
        #s.software_pic.name = "album_pictures/software/" + jpg_name
        #s.save()
    for s in Album.objects.all():
        pic_id = str((s.id-21) % 6)
        pic_path = pic_id + "_" + s.language_code.lang_code + ".jpg"
        s.cover_pic.name = "album_pictures/cover/" + pic_path
        s.save()

if __name__ == '__main__':
    #alter_language()
    append_picture()
