#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os
import sys
sys.path.append(os.curdir)

SITEURL = 'http://www.matthieukeller.com/blog/'
RELATIVE_URLS = False

# DELETE_OUTPUT_DIRECTORY = True

AUTHOR = u'Matthieu Keller'
SITENAME = u"maggick's logs"

PATH = 'content'
DISPLAY_PAGES_ON_MENU = "True"
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
          ('Linked In', 'https://linkedin.com/in/matthieukeller'),
          ('RSS / ATOM feed',
           'http://www.matthieukeller.com/blog/feeds/all.atom.xml'),
          ('Notes', 'www.matthieukeller.com/notes'),
          )

# Menu - NOT WORKING
MENUITEMS = (
             ('Portal', 'www.matthieukeller.com'),
             ('Blog', '/'),
             ('Notes', 'www.matthieukeller.com/notes'),
            )

DEFAULT_PAGINATION = 10

THEME = "/home/maggick/work/pelican-themes/maggner-pelican/"
STATIC_PATHS = ['images']

# Third party
DISQUS_SITENAME = "matthieukeller"
# GOOGLE_ANALYTICS = ""

# License
LICENSE = 'Creative Commons Attribution 4.0'
LICENSE_URL = 'http://creativecommons.org/licenses/by-sa/4.0/'
LICENSE_TITLE = 'Share, adapt, use.\
        But mention the author and keep the same license'
SOURCE_CODE_URL = 'https://github.com/maggick/blog/'
SOURCE_CODE_REPOSITORY = 'GitHub'
