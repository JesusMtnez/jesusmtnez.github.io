#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# Main Configuration
AUTHOR = 'JesusMtnez'
SITEURL = 'http://127.0.0.1:8000'
SITENAME = 'JesusMtnez\'s Blog'
SITETITLE = 'Blog de Jesús Martínez-B. H.'
SITESUBTITLE = 'Backend Developer'
SITELOGO = '/images/profile.jpeg'
SITEDESCRIPTION = 'Historias de un programador ávido de conocimiento'
TIMEZONE = 'Europe/Madrid'
COPYRIGHT_YEAR = 2017
DATE_FORMATS = {
  'es': '%d / %m / %Y'
}
I18N_TEMPLATES_LANG = 'en'
DEFAULT_LANG = 'es'
OG_LOCALE = 'es_ES'
LOCALE = 'es_ES.UTF-8'
JINJA_ENVIRONMENT = {
  'extensions': ['jinja2.ext.i18n']
}
PLUGINS = ['i18n_subsites']

# PATHs
PATH = 'content'
OUTPUT_PATH = 'public'
PAGE_PATHS = ['pages']
ARTICLE_PATHS = ['articles']
STATIC_PATHS = ['images', 'extra']
PLUGIN_PATHS = ['pelican-plugins']

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Social widget
SOCIAL = (
  ('twitter', 'https://twitter.com/JesusMtnezBH'),
  ('linkedin', 'https://linkedin.com/in/JesusMtnez'),
  ('gitlab', 'https://gitlab.com/JesusMtnez'),
  ('github', 'https://github.com/JesusMtnez')
)

# Theme settings
THEME = "Flex"
PYGMENTS_STYLE = 'native'
TYPOGRIFY = True
DEFAULT_PAGINATION = 10
SUMMARY_MAX_LENGTH = 50

# Menu settings
MAIN_MENU = True
MENUITEMS = (
  ('Archivo', '/archives.html'),
  ('Categorias', '/categories.html')
)

# URLs
AUTHOR_URL = ''
AUTHOR_SAVE_AS = ''

# Other settings
USE_FOLDER_AS_CATEGORY = False
DISPLAY_PAGES_ON_MENU = True
