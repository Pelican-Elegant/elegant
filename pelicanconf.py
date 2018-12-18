#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Pelican Elegant Team'
SITENAME = u"Elegant Documentation"
SITEURL = '/'

# Regional Settings
TIMEZONE = 'Asia/Karachi'
DATE_FORMATS = {'en': '%b %d, %Y'}
DEFAULT_LANG = u'en'

# Plugins and extensions
MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {
            'css_class': 'highlight'
        },
        'markdown.extensions.extra': {},
        'markdown.extensions.toc': {
            'permalink': 'true'
        },
        'markdown.extensions.meta': {},
        'markdown.extensions.admonition': {}
    }
}

PLUGIN_PATHS = ['plugins/']
PLUGINS = ['sitemap', 'extract_toc', 'tipue_search', 'liquid_tags.img',
           'neighbors', 'render_math', 'related_posts', 'assets', 'share_post',
           'series']
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}

# Appearance
TYPOGRIFY = False
THEME = 'themes/elegant'
DEFAULT_PAGINATION = False

# Defaults
DEFAULT_CATEGORY = 'Miscellaneous'
USE_FOLDER_AS_CATEGORY = False
ARTICLE_URL = u'{slug}'
PAGE_URL = u'{slug}'
PAGE_SAVE_AS = u'{slug}.html'

# Feeds
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Social
SOCIAL = (('Twitter', 'http://twitter.com/talham_'),
          ('Github', 'http://github.com/talha131'),
          ('GitTip', 'http://gittip.com/talha131'),
          ('Email', 'mailto:talha131@gmail.com'),)

# Elegant theme
STATIC_PATHS = ['theme/images', 'images', 'extra/google3bc953001343abe6', 'extra/robots.txt']
EXTRA_PATH_METADATA = {
    'extra/google3bc953001343abe6' : {'path': 'google3bc953001343abe6.html'},
    'extra/robots.txt': {'path': 'robots.txt'}
}
DIRECT_TEMPLATES = (('index', 'tags', 'categories', 'archives', 'search', '404'))
TAG_SAVE_AS = ''
AUTHOR_SAVE_AS = ''
CATEGORY_SAVE_AS = ''
USE_SHORTCUT_ICONS = True

# Elegant Labels
SOCIAL_PROFILE_LABEL = u'Stay in Touch'
RELATED_POSTS_LABEL = 'Keep Reading'
SHARE_POST_INTRO = 'Like this post? Share on:'
COMMENTS_INTRO = u'So what do you think? Did I miss something? Is any part unclear? Leave your comments below.'

# Mailchimp
EMAIL_SUBSCRIPTION_LABEL = u'Get Monthly Updates'
EMAIL_FIELD_PLACEHOLDER = u'Enter your email...'
SUBSCRIBE_BUTTON_TITLE = u'Send me Free updates'
MAILCHIMP_FORM_ACTION = u'empty'

# SMO
TWITTER_USERNAME = u''
FEATURED_IMAGE = SITEURL + '/theme/images/apple-touch-icon-152x152.png'

# Legal
SITE_LICENSE = u'Elegant theme documentation is licensed under a CC-BY-SA-4.0 license.'

# SEO
SITE_DESCRIPTION = u'Documentation website for Pelican-Elegant theme originally created by Talha Mansoor'

# Landing Page
PROJECTS = [{'name': 'Elegant', 'url': 'https://github.com/Pelican-Elegant/elegant',
             'description': 'A clean and distraction free Pelican theme, with search and a lot more unique features. Built with Jinja2 and Bootstrap'},
            {'name': 'Elegant Documentation', 'url': 'https://github.com/Pelican-Elegant/documentation',
             'description': 'Documentation repository for Pelican-Elegant theme'}]

LANDING_PAGE_ABOUT = {'title': 'Live demonstration and documentation of Pelican-Elegant Theme',
                      'details': """<p>This page serves both as documentation site and demonstration of Pelican-Elegant theme capabilities and look&amp;feel.</p><p>Please do check our Project pages and browse this site for more information.</p>"""}
