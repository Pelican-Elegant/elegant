#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Talha Mansoor'
SITENAME = u"<span style=\'color:black;\'>onCrash</span> <span style=\'color:darkblue;\'>=</span> <span style=\'color:#AA1032;\'>'reboot();'</span>"

# Regional Settings
TIMEZONE = 'Asia/Karachi'
DATE_FORMATS = {'en': '%b %d,  %Y'}
DEFAULT_LANG = u'en'

# Plugins and extensions
MD_EXTENSIONS = ['codehilite(css_class=highlight)', 'extra', 'headerid']
PLUGIN_PATH = "../pelican-plugins/"
PLUGINS = ['sitemap', 'extract_toc', 'content_in_json']

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
TYPOGRIFY = True
THEME = "elegant"
DEFAULT_PAGINATION = False

# Defaults
DEFAULT_CATEGORY = "Miscellaneous"

# Feeds
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Elegant theme
RECENT_ARTICLES_COUNT = 10
COMMENTS_INTRO = u"So what do you think? Got something to say about the post? Did I miss something? Leave your comments below."
SITE_LICENSE = u"Copyright © 2013 <a href=\"http://oncrashreboot.com\" title=\"Talha Mansoor Home Page\">Talha Mansoor</a>. All Rights Reserved." 
DIRECT_TEMPLATES = (('index', 'tags', 'categories','archives', 'search', '404'))
SITE_DESCRIPTION = u"Personal blog of Talha Mansoor"
EMAIL_SUBSCRIPTION_LABEL = u'Get Monthly Updates'
EMAIL_FIELD_PLACEHOLDER = u'Enter your email...'
SUBSCRIBE_BUTTON_TITLE = u'Send me Free updates'
MAILCHIMP_FORM_ACTION = u'http://oncrashreboot.us4.list-manage2.com/subscribe/post?u=e66b4cca51e40b859c64e8411&amp;id=d135692a12'
DISQUS_SITENAME = u'oncrashreboot'
PROJECTS = [{'name': 'Twitter Followers Growth',
            'url': 'https://github.com/talha131/twitter-followers-growth',
            'description': 'Keeps track of twitter followers and generate a '
            'timeline to show the change over time.'},
            {'name': 'Elegant',
            'url': 'https://github.com/talha131/pelican-elegant',
            'description': 'A theme for pelican using Bootstrap and Jinja2. '
            'Under development'},
           {'name': 'Logpad + Duration',
            'url': 'https://github.com/talha131/twitter-followers-growth',
            'description': 'Vim plugin'} ]
LANDING_PAGE_ABOUT = {'title': 'I design and build software products for iOS and OSX',
        'details': '<p>My name is Talha Mansoor. I am <a href=\"https://github.com/talha131/\" title=\"My Github profile\">talha131</a> at Github and <a href=\"https://twitter.com/talham_/\" title=\"My Twitter profile\">@talham_</a> at twitter. You can also reach me via <a href=\"mailto:talha131@gmail.com\" title=\"My email address\">email</a>.</p><p>I work on <a href=\"http://jumpdesktop.com/\" title=\"Jump Desktop\">Jump Desktop</a> which is a remote desktop application for iOS, OSX and Android. I play a broad role there - which includes research, product design, engineering and deployment. I also lend a hand in user support.</p><p>I try to contribute to society by striving to create great software products that make people\'s lives easier. I believe software is the most effective way to touch others\' lives in our day and time.</p><p>I mostly work in C, C++ and Objective-C on OSX and Linux, I also dabble in Python, Vim-L and JavaScript. I do not pigeonhole myself to specific languages or frameworks. A good developer is receptive and has the ability to learn new technologies. I also often contribute to open source projects and beta test startup products.</p><p>Besides programming, I <a href=\"https://www.fitocracy.com/profile/Andrew-Dufresne/\" title=\"My Fitocracy profile\">exercise</a> and <a href=\"http://www.goodreads.com/talham\" title=\"My GoodReads profile\">read books</a> regularly. To be a stronger and better version of myself!</p><p>English is my second language. I am also learning <a href=\"http://www.duolingo.com/talham\" title=\"My Duolingo profile\">German from Duolingo</a>.</p>'
                    }
