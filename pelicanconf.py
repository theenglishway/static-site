#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'theenglishway'
SITENAME = u'theenglishway'
SITEURL = 'theenglishway.eu'

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'fr'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = ()

# Social widget
SOCIAL = (('My GitHub', 'https://github.com/theenglishway'),
          ('My Twitter', 'https://twitter.com/the_english_way'))

DEFAULT_PAGINATION = False
#THEME = 'themes/pelican-alchemy/alchemy'
THEME = 'notmyidea'
SITEIMAGE = 'images/theenglishway_profile.jpg'
SITESUBTITLE = "Thought I'd've something more to say"
DEFAULT_DATE = 'fs'
TWITTER_USERNAME = 'the_english_way'

FEED_RSS = 'feeds/all.rss.xml'

ISSO_SERVER = "http://comments.theenglishway.eu"

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

DEFAULT_METADATA = {
    'status': 'draft',
}
