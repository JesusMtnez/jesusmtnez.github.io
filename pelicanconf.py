#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'JesusMtnez'
SITEURL = ''
SITENAME = "JesusMtnez's Blog"
SITELOGO = SITEURL + '/images/profile.jpeg'

PATH = 'content'
OUTPUT_PATH = 'public'
TIMEZONE = 'Europe/Madrid'
DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Social widget
SOCIAL = (('twitter', 'https://twitter.com/JesusMtnezBH'),
	  ('linkedin', 'https://linkedin.com/in/JesusMtnez'),
          ('gitlab', 'https://gitlab.com/JesusMtnez'),
          ('github', 'https://github.com/JesusMtnez')
         )

DEFAULT_PAGINATION = 10

# Theme settings
THEME = "Flex"
BIO = "Desarrollador backend, aprendiz de Scala, escritor novato"
PROFILE_IMAGE = "avatar.jpeg"
