#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)

SITEURL = 'http://www.matthieukeller.com/blog/'
# RELATIVE_URLS = False

FEED_ATOM = 'feeds/all.atom.xml'
FEED_MAX_ITEMS = 5

# DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing
DISQUS_SITENAME = "matthieukeller"
# GOOGLE_ANALYTICS = ""

AUTHOR = u'Matthieu Keller'
SITENAME = u"maggick's logs"
SITEURL = '/blog'

DISPLAY_PAGES_ON_MENU = "True"
PATH = 'content'
ARTICLE_EXCLUDES = ('pages',)
PAGE_URL = 'pages/{slug}.html'

TIMEZONE = 'Europe/Paris'
DEFAULT_DATE_FORMAT = '%d %b %Y'

DEFAULT_LANG = 'en'

# Article
ARTICLE_URL = '{date:%Y}/{date:%m}/{slug}.html'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{slug}.html'

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),)

# Social widget
SOCIAL = (('Github', 'https://github.com/maggick'),
          ('Twitter', 'https://twitter.com/matthieukeller'),
          ('Linked In', 'https://linkedin.com/in/matthieukeller')
          )

# Menu
MENUITEMS = (
  ('Portal', 'www.matthieukeller.com'),
  ('Blog', '/'),
  ('Notes', 'www.matthieukeller.com/notes'),
)

DEFAULT_PAGINATION = 10

THEME = "/home/maggick/work/pelican-themes/maggner-pelican/"
STATIC_PATHS = ['images']

# Following items are often useful when publishing
DISQUS_SITENAME = "matthieukeller"
# GOOGLE_ANALYTICS = ""

# License
LICENSE = 'Creative Commons Attribution 4.0'
LICENSE_URL = 'http://creativecommons.org/licenses/by-sa/4.0/'
LICENSE_TITLE = 'Share, adapt, use.\
        But mention the author and keep the same license'
SOURCE_CODE_URL = 'https://github.com/maggick/blog/'
SOURCE_CODE_REPOSITORY = 'GitHub'
