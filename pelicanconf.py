#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Matthieu Keller'
SITENAME = "maggick's logs"
SITEURL = '/blog'

PATH = 'content'

TIMEZONE = 'Europe/Paris'
DEFAULT_DATE_FORMAT='%d %b %Y'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Article
ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}.html'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}.html'

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

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = "/home/maggick/Documents/pelican-themes/maggner-pelican/"
STATIC_PATHS = ['images']

# Following items are often useful when publishing
DISQUS_SITENAME = "matthieukeller"
#GOOGLE_ANALYTICS = ""

# License
LICENSE = 'Creative Commons Attribution 4.0'
LICENSE_URL = 'http://creativecommons.org/licenses/by-sa/4.0/'
LICENSE_TITLE = 'Share, adapt, use. But mention the author and keep the same license'
SOURCE_CODE_URL = 'https://github.com/maggick/blog/'
SOURCE_CODE_REPOSITORY = 'GitHub'

