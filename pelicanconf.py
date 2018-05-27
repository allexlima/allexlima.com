#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals


THEME = './theme'
PATH = './content'

SITENAME = 'Allex Lima'

AUTHOR = 'Allex'
AUTHOR_DESCRIPTION = "Blablabla"

ARTICLE_PATHS = ['blog']
ARTICLE_SAVE_AS = 'blog/{slug}.html'
ARTICLE_URL = 'blog/{slug}.html'

STATIC_PATHS = ['thumbs', 'extra', 'blog', 'projects', 'research']
EXTRA_PATH_METADATA = {
    'extra/favicon.ico': {'path': 'favicon.ico'},
}

# For dev mode
SITEURL = 'http://199.7.9.1:8000'

TIMEZONE = 'America/Manaus'
DEFAULT_LANG = 'en'
DEFAULT_DATE_FORMAT = "%a, %d %b %Y"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None


# ---------------- Website Internal setting ---
MENUS = (('Welcome', '#welcome'),
         ('Posts', '#posts'),
         ('Research', '#research'),
         ('Projects', '#projects'),
         ('Get in touch', '#contact'))

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False
