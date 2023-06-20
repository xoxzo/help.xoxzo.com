#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import os

HERE = os.path.abspath(os.path.dirname(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(HERE, '.'))

SITENAME = 'Xoxzo Help Center'
SITEURL = 'http://localhost:8000'

PATH = 'content'

TIMEZONE = 'Asia/Tokyo'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

DEFAULT_DATE_FORMAT = "%Y-%m-%d"
STATIC_PATHS = ['images', 'pdfs', 'extra/CNAME', '_redirects', 'extra/robots.txt']
EXTRA_PATH_METADATA = {
        'extra/CNAME': {'path': 'CNAME'},
        'extra/robots.txt': {'path': 'robots.txt'},
        '_redirects': {'path': '_redirects'},
    }

#THEME           = 'themes/simple'
THEME           = 'themes/xoxzo'
PLUGIN_PATHS    = [os.path.join(PROJECT_ROOT, 'plugins'),]
PLUGINS         = ["i18n_subsites", "subcategory", "more_categories", "tipue_search", "sitemap", "netlify_redirect"]
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n',]}

DIRECT_TEMPLATES = (('index', 'search'))

I18N_UNTRANSLATED_ARTICLES  = "remove"
I18N_UNTRANSLATED_PAGES     = "keep"
I18N_GETTEXT_LOCALEDIR = 'locales'

I18N_SUBSITES   = {
    'en': {
        'STATIC_PATHS': STATIC_PATHS,
        'THEME_STATIC_PATHS': STATIC_PATHS + ['static'],
    },
    'ja': {
        'SITENAME': 'Xoxzoのヘルプセンター',
        'STATIC_PATHS': STATIC_PATHS,
        'THEME_STATIC_PATHS': STATIC_PATHS + ['static'],
    },
}

DATE_FORMATS = {
    'en': DEFAULT_DATE_FORMAT,
    'ja': DEFAULT_DATE_FORMAT,
}

PATH_METADATA= '(?P<subcategory_path>.*)/.*'

ARTICLE_URL = '{category}/articles/{slug}/'
ARTICLE_LANG_URL = '{lang}/{category}/articles/{slug}/'
ARTICLE_SAVE_AS = '{category}/articles/{slug}/index.html'
PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS = 'pages/{slug}/index.html'
CATEGORY_URL = '{slug}/'
CATEGORY_SAVE_AS = '{slug}/index.html'
SUBCATEGORY_URL = '{savepath}/'
SUBCATEGORY_SAVE_AS = '{savepath}/index.html'
TAG_URL = 'tag/{slug}/'
TAG_SAVE_AS = 'tag/{slug}/index.html'

REVERSE_CATEGORY_ORDER = True

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'weekly',
    }
}

from datetime import date
CURRENTYEAR = date.today().year

NETLIFY_REDIRECTS = [
    ("/ja/ezsms-sms-delivery-service/articles/what-are-the-variables-that-i-can-use-for-return-sms-with-dialsms/", "https://help.xoxzo.com/ja/ezsms-sms-delivery-service/sms-api/articles/what-are-the-variables-that-i-can-use-for-return-sms-with-dialsms/", 302),
    ("/ja/ezsms-sms-delivery-service/articles/mobile-number-authentication/", "https://help.xoxzo.com/ja/ezsms-sms-delivery-service/account/articles/mobile-number-authentication/", 302),
    ("/ja/ezsms-sms-delivery-service/articles/what-will-be-displayed-as-senderid-of-the-dialsms-message/", "https://help.xoxzo.com/ja/ezsms-sms-delivery-service/sms-api/articles/what-will-be-displayed-as-senderid-of-the-dialsms-message/", 302),
    ("/ja/ezsms-sms-delivery-service/articles/how-to-send-with-customised-csv/", "https://help.xoxzo.com/ja/ezsms-sms-delivery-service/sms/articles/how-to-send-with-customised-csv/", 302),
    ("/ja/ezsms-sms-delivery-service/articles/how-many-characters-would-fit-within-1-x-sms/", "https://help.xoxzo.com/ja/ezsms-sms-delivery-service/sms-api/articles/how-many-characters-would-fit-within-1-x-sms/", 302),
    ("/ja/ezsms-sms-delivery-service/articles/can-i-send-sms-to-au-phones-via-c-mail/", "https://help.xoxzo.com/ja/ezsms-sms-delivery-service/sms-api/articles/can-i-send-sms-to-au-phones-via-c-mail/", 302),
    ("/en/ezsms-sms-delivery-service/articles/what-are-the-variables-that-i-can-use-for-return-sms-with-dialsms/", "https://help.xoxzo.com/en/ezsms-sms-delivery-service/sms-api/articles/what-are-the-variables-that-i-can-use-for-return-sms-with-dialsms/", 302),
    ("/en/ezsms-sms-delivery-service/articles/mobile-number-authentication/", "https://help.xoxzo.com/en/ezsms-sms-delivery-service/account/articles/mobile-number-authentication/", 302),
    ("/en/ezsms-sms-delivery-service/articles/what-will-be-displayed-as-senderid-of-the-dialsms-message/", "https://help.xoxzo.com/en/ezsms-sms-delivery-service/sms-api/articles/what-will-be-displayed-as-senderid-of-the-dialsms-message/", 302),
    ("/en/ezsms-sms-delivery-service/articles/how-to-send-with-customised-csv/", "https://help.xoxzo.com/en/ezsms-sms-delivery-service/sms-api/articles/how-to-send-with-customised-csv/", 302),
    ("/en/ezsms-sms-delivery-service/articles/how-many-characters-would-fit-within-1-x-sms/", "https://help.xoxzo.com/en/ezsms-sms-delivery-service/sms-api/articles/how-many-characters-would-fit-within-1-x-sms/", 302),
    ("/en/ezsms-sms-delivery-service/articles/can-i-send-sms-to-au-phones-via-c-mail/", "https://help.xoxzo.com/en/ezsms-sms-delivery-service/sms-api/articles/can-i-send-sms-to-au-phones-via-c-mail/", 302),
]
