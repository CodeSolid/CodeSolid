#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'John Lockwood'
SITENAME = 'CodeSolid'
SITESUBTITLE = 'I make being me look easy.'
#SITEURL = 'http://codesolid.com/'

PATH = 'content'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
#LINKS = (('Pelican', 'http://getpelican.com/'),
#         ('Python.org', 'http://python.org/'),
#         ('Jinja2', 'http://jinja.pocoo.org/'),
#         ('You can modify those links in your config file', '#'),)
# ("Sacramento Tech Coop (Meetup)", "/sacramento_tech_coop.html"),
MENUITEMS = [("Projects", "/goalboost.html"), ("The License", "/license.html"), ("Contribute", "/contribute.html"), ("Foundations", "/foundations.html"), ("Blog", "/blog.html") ]

GITHUB_URL = 'https://github.com/CodeSolid'
TWITTER_URL = 'https://twitter.com/JohnLockwood'
FACEBOOK_URL = ''
GOOGLEPLUS_URL = ''

# Social widget

SOCIAL = [ 	('http://twitter.com/JohnLockwood', 'twitter.png'), \
			('https://www.linkedin.com/in/codesolid', 'linkedin.png'), \
			('http://github.com/CodeSolid', 'github.png'), \
			('http://stackoverflow.com/users/161644/john-lockwood', 'so-icon-small.png') \
		 ]          

DEFAULT_PAGINATION = 6


THEME="./themes/codesolid"


#PLUGIN_PATHS = ["plugins", "/home/john/Dropbox/source/pelican-plugins/"]
#PLUGINS = ["code_include"]

INDEX_SAVE_AS = 'blog.html'


FOUNDATION_FRONT_PAGE_FULL_ARTICLES = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
