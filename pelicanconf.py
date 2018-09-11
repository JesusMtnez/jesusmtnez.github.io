#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# Main Configuration
AUTHOR = 'JesusMtnez'
SITEURL = 'http://127.0.0.1:8000'
SITENAME = 'JesusMtnez\'s Blog'
SITETITLE = 'JesusMtnez\'s personal blog'
SITESUBTITLE = 'Scala developer & Functional programmer enthusiast & DevOps'
SITELOGO = '/images/profile.jpeg'
SITEDESCRIPTION = 'My place to share all my adventures as developer'
TIMEZONE = 'Europe/Madrid'
COPYRIGHT_YEAR = 2017

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
PYGMENTS_STYLE = 'solarized-dark'
MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {
            'css_class': 'highlight',
            'guess_lang': False
        },
        'markdown.extensions.extra': {},
        #'markdown.extensions.meta': {},
    },
    'output_format': 'html5',
}
TYPOGRIFY = True
DEFAULT_PAGINATION = 10
SUMMARY_MAX_LENGTH = 50

# Menu settings
MAIN_MENU = True
MENUITEMS = (
    ('Archive', '/archives.html'),
    ('Categories', '/categories.html'),
)

# URLs
AUTHOR_URL = ''
AUTHOR_SAVE_AS = ''
DISABLE_URL_HASH = True

#LANG Settings
DATE_FORMATS = {
    'en': '%Y / %m / %d'
}

I18N_TEMPLATES_LANG = 'en'
DEFAULT_LANG = 'en'
LOCALE = 'en_US'

# Other settings
USE_FOLDER_AS_CATEGORY = False
DISPLAY_PAGES_ON_MENU = True
DEFAULT_PAGINATION = 10
DISQUS_SITENAME = 'jesusmtnez-gitlab-blog'
