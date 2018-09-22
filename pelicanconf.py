#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'theenglishway'
SITENAME = u'theenglishway'
SITEURL = u'http://localhost:8000'

SITETITLE = 'theenglishway'
SITESUBTITLE = "Thought I'd've something more to say"
SITELOGO = '/images/theenglishway_profile.jpg'
FAVICON = '/images/favicon.ico'

BROWSER_COLOR = '#333'

PATH = 'content'

TIMEZONE = 'Europe/Paris'

PLUGIN_PATHS = [u'pelican-plugins']
PLUGINS = ['i18n_subsites', 'representative_image', 'sitemap']

JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}

ROBOTS = 'index, follow'
SITEMAP = {
    'format': 'xml',
    'exclude': ['tag/', 'category/']
}

I18N_TEMPLATES_LANG = 'en'
DEFAULT_LANG = 'fr'
OG_LOCALE = 'fr_FR'
LOCALE = 'fr_FR'

I18N_SUBSITES = {
    'fr': {
        'THEME_STATIC_DIR': 'themes',
        'STATIC_PATHS': ['images']
    },
    'en': {
        'THEME_STATIC_DIR': 'themes',
        'STATIC_PATHS': ['images']
    }
}

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

USE_FOLDER_AS_CATEGORY = False
MAIN_MENU = True
HOME_HIDE_TAGS = True
PAGE_ORDER_BY = 'priority'
PAGES_SORT_ATTRIBUTE = 'priority'

MENUITEMS = (('Archives', '/archives.html'),
             ('Categories', '/categories.html'),
             ('Tags', '/tags.html'),)

# Blogroll
LINKS = ()

# Social widget
SOCIAL = (('github', 'https://github.com/theenglishway'),
          ('twitter', 'https://twitter.com/the_english_way'),
          ('rss', '//blog.theenglishway.eu/feeds/all.atom.xml'))

CC_LICENSE = {
    'name': 'Creative Commons Attribution-NonCommercial-ShareAlike',
    'version': '4.0',
    'slug': 'by-nc-sa'
}

DEFAULT_PAGINATION = False
THEME = 'themes/Flex'
DEFAULT_DATE = 'fs'
STATIC_PATHS = ['images', 'extra/robots.txt']
EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
}
THEME_STATIC_DIR = 'themes'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

DEFAULT_METADATA = {
    'status': 'draft',
}
