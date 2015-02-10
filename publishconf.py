#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
from pelicanconf import *
sys.path.append(os.curdir)

SITEURL = 'http://www.matthieukeller.com/blog/'
# RELATIVE_URLS = False

FEED_DOMAIN = SITEURL
FEED_ATOM = 'rss'

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing
DISQUS_SITENAME = "matthieukeller"
# GOOGLE_ANALYTICS = ""
