#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

deploy_context = os.environ.get('CONTEXT', '')

SITEURL = 'https://help.xoxzo.com'

if deploy_context != 'production':
    SITEURL = os.environ.get("DEPLOY_URL", SITEURL)

RELATIVE_URLS = False

FEED_DOMAIN = SITEURL
FEED_ALL_RSS = None
CATEGORY_FEED_RSS = None
TRANSLATION_FEED_RSS = None

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing

#DISQUS_SITENAME = ""
#GOOGLE_ANALYTICS = ""
