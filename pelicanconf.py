#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Talha Mansoor'
SITENAME = u"<span style=\'color:black;\'>onCrash</span> <span style=\'color:darkblue;\'>=</span> <span style=\'color:#AA1032;\'>'reboot();'</span>"
SITEURL = 'http://localhost:8000'

# Regional Settings
TIMEZONE = 'Asia/Karachi'
DATE_FORMATS = {'en': '%b %d,  %Y'}
DEFAULT_LANG = u'en'

# Plugins and extensions
MD_EXTENSIONS = ['codehilite(css_class=highlight)', 'extra', 'headerid', 'toc']
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
COMMENTS_INTRO = u"So what do you think? Did I miss something? Is any part unclear? Leave your comments below."
SITE_LICENSE = u"<span xmlns:dct=\"http://purl.org/dc/terms/\" property=\"dct:title\"> onCrash=\"Reboot();\"</span> by <a xmlns:cc=\"http://creativecommons.org/ns#\" href=\"http://oncrashreboot.com\" property=\"cc:attributionName\" rel=\"cc:attributionURL\">Talha Mansoor</a> is licensed under a <a rel=\"license\" href=\"http://creativecommons.org/licenses/by-sa/3.0/deed.en_US\">Creative Commons Attribution-ShareAlike 3.0 Unported License</a>." 
DIRECT_TEMPLATES = (('index', 'tags', 'categories','archives', 'search', '404'))
SITE_DESCRIPTION = u"Personal blog of Talha Mansoor"
EMAIL_SUBSCRIPTION_LABEL = u'Get Monthly Updates'
EMAIL_FIELD_PLACEHOLDER = u'Enter your email...'
SUBSCRIBE_BUTTON_TITLE = u'Send me Free updates'
MAILCHIMP_FORM_ACTION = u'http://oncrashreboot.us4.list-manage2.com/subscribe/post?u=e66b4cca51e40b859c64e8411&amp;id=d135692a12'
PROJECTS = [{
    'name': 'Pelican Plugins',
    'url':
    'https://github.com/getpelican/pelican-plugins/commits?author=talha131',
    'description': 'A bunch of plugins for the Pelican blog engine'},
    {
        'name': 'Asana to Github Issues',
        'url': 'https://github.com/talha131/AsanaToGithub#asana-to-github',
        'description': 'Command-line program to move your tasks from Asana'
        ' projects to Github issues'},
    {
        'name': 'Logpad + Duration',
        'url':
        'https://github.com/talha131/logpad-plus-duration#logpad--duration',
        'description': 'Vim plugin to emulate Windows Notepad logging feature,'
        ' and log duration of each entry'},
    {
        'name': 'Elegant Theme for Pelican',
        'url':
        'http://oncrashreboot.com/pelican-elegant',
        'description': 'A clean and distraction free theme, with search and a'
        ' lot more unique features, using Jinja2 and Bootstrap'},
    {
        'name': 'Pelican',
        'url':
        'https://github.com/getpelican/pelican/commits?author=talha131',
        'description': 'Static site generator that supports Markdown and'
        ' reST syntax'},
    {
        'name': 'Asana',
        'url':
        'https://github.com/pandemicsyn/asana/commits?author=talha131',
        'description': 'Python Asana API bindings'},
    {
        'name': 'Wasavi',
        'url':
        'https://github.com/akahuku/wasavi/commits?author=talha131',
        'description': 'A browser extension that changes textarea element to'
        ' Vi editor'
        }]
LANDING_PAGE_ABOUT = {'title': 'I design and build software products for iOS and OSX',
        'details': '<p>My name is Talha Mansoor. I am <a href=\"https://github.com/talha131/\" title=\"My Github profile\">talha131</a> at Github and <a href=\"https://twitter.com/talham_/\" title=\"My Twitter profile\">@talham_</a> at twitter. You can also reach me via <a href=\"mailto:talha131@gmail.com\" title=\"My email address\">email</a>.</p><p>I work on <a href=\"http://jumpdesktop.com/\" title=\"Jump Desktop\">Jump Desktop</a> which is a remote desktop application for iOS, OSX and Android. I play a broad role there - which includes research, product design, engineering and deployment. I also lend a hand in user support.</p><p>I try to contribute to society by striving to create great software products that make people\'s lives easier. I believe software is the most effective way to touch others\' lives in our day and time.</p><p>I mostly work in C, C++ and Objective-C on OSX and Linux, I also dabble in Python, Vim-L and JavaScript. I do not pigeonhole myself to specific languages or frameworks. A good developer is receptive and has the ability to learn new technologies. I also often contribute to open source projects and beta test startup products.</p><p>Besides programming, I <a href=\"https://www.fitocracy.com/profile/Andrew-Dufresne/\" title=\"My Fitocracy profile\">exercise</a> and <a href=\"http://www.goodreads.com/talham\" title=\"My GoodReads profile\">read books</a> regularly. To be a stronger and better version of myself!</p><p>English is my second language. I am also learning <a href=\"http://www.duolingo.com/talham\" title=\"My Duolingo profile\">German from Duolingo</a>.</p>'
                    }
STATIC_PATHS = ['theme/images', 'images']
TAG_SAVE_AS = ''
CATEGORY_SAVE_AS = ''
AUTHOR_SAVE_AS = ''
