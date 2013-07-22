#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dsc_home_manager.settings")

from deepin_utils.file import get_parent_dir
from album.models import Software, Album
import json

data_dir = os.path.join(get_parent_dir(__file__, 2), "deepin-software-center-service-private", "dsc-home-data", "input_data")
album_dir = os.path.join(data_dir, "album")
album_pic_dir = os.path.join(data_dir, "data", "home", "album_picture")

for a in Album.objects.all():
    a.delete()

for s in Software.objects.all():
    s.delete()

for lang in os.listdir(data_dir):
    if lang in ['zh_CN', 'zh_TW', 'en_US']:
        js_file = os.path.join(album_dir, lang, "album_contents.json")
        try:
            with open(js_file) as fp:
                contents = json.load(fp)
        except:
            print "Load js data failed: ", js_file

        for album in contents:
            al = Album(
                    language=lang.lower(),
                    name=album['name'],
                    summary=album['summary'],
                    )
            al.save()

            for soft in album['contents']:
                s = Software(
                        pkg_name=soft['pkg_name'],
                        language=lang.lower(),
                        display_name=soft['pkg_name'],
                        short_desc=soft['short_desc'],
                        long_desc=soft['long_desc'],
                        )
                s.save()
                al.softwares.add(s)
            al.save()
