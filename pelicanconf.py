#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os
import sys
sys.path.append(os.curdir)

SITEURL = 'https://matthieukeller.com'
RELATIVE_URLS = False

# DELETE_OUTPUT_DIRECTORY = True

AUTHOR = u'maggick'
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
DISPLAY_CATEGORIES_ON_MENU = True

# Plugins
PLUGIN_PATHS = ['./pelican-plugins/']
PLUGINS = ['summary', 'Better code samples']
#MARKDOWN = {'extensions':['markdown.extensions.codehilite(css_class=highlight)', 'markdown.extensions.extra', 'markdown.extensions.toc']}

# Social
# Social widget
SOCIAL = (('github', 'https://github.com/maggick'),
          ('twitter', 'https://twitter.com/matthieukeller'),
          ('linkedin', 'https://linkedin.com/in/matthieukeller'),
          ('stackoverflow', 'http://stackoverflow.com/users/1827067/maggick'),
          )

# Menu
MENUITEMS = (
             ('archives', '/archives'),
             ('feeds', '/feeds/all.atom.xml'),
             ('links', '/pages/links.html'),
            )

DEFAULT_PAGINATION = 10

THEME = "./maggner-pelican/"
STATIC_PATHS = ['media', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}
FAVICON_URL = "%s/media/favicon.ico" % SITEURL

# Third party
DISQUS_SITENAME = "matthieukeller"
GOOGLE_ANALYTICS = "UA-63314567-1"

# License
LICENSE = 'Creative Commons Attribution 4.0'
LICENSE_URL = 'http://creativecommons.org/licenses/by-sa/4.0/'
LICENSE_TITLE = 'Share, adapt, use.\
        But mention the author and keep the same license'
SOURCE_CODE_URL = 'https://github.com/maggick/blog/'
SOURCE_CODE_REPOSITORY = 'GitHub'
