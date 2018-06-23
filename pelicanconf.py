#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# Main Configuration
AUTHOR = 'JesusMtnez'
SITEURL = 'http://127.0.0.1:8000'
SITENAME = 'JesusMtnez\'s Blog'
SITETITLE = 'Blog de Jesús Martínez'
SITESUBTITLE = 'Scala developer & Functional programmer enthusiast & DevOps'
SITELOGO = '/images/profile.jpeg'
SITEDESCRIPTION = 'Historias de un programador ávido de conocimiento'
TIMEZONE = 'Europe/Madrid'
COPYRIGHT_YEAR = 2017

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
    ('Categorias', '/categories.html'),
    ('English', '/en/')
)

# URLs
AUTHOR_URL = ''
AUTHOR_SAVE_AS = ''
DISABLE_URL_HASH = True

#LANG Settings
DATE_FORMATS = {
    'es': '%d / %m / %Y',
    'en': '%Y / %m / %d'
}

I18N_TEMPLATES_LANG = 'en'
DEFAULT_LANG = 'es'
LOCALE = 'es_ES'

I18N_SUBSITES = {
    'en': {
        'SITETITLE': 'Jesús Martínez Blog',
        'SITEDESCRIPTON': 'A developer\'s blog',
        'MENUITEMS': (
            ('Archive', '/en/archives.html'),
            ('Categories', '/en/categories.html'),
            ('Spanish', '/')
        )
    }
}


# Other settings
USE_FOLDER_AS_CATEGORY = False
DISPLAY_PAGES_ON_MENU = True
DEFAULT_PAGINATION = 10
DISQUS_SITENAME = 'jesusmtnez-gitlab-blog'
