#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = 'https://jesusmtnez.gitlab.io'
RELATIVE_URLS = False

THEME = '/tmp/flex-pelican-theme'
PLUGIN_PATHS = ['/tmp/pelican-plugins']

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'

DELETE_OUTPUT_DIRECTORY = True
OUTPUT_PATH = 'public'

GOOGLE_ANALYTICS = 'UA-121213323-1'
