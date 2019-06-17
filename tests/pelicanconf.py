#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Talha Mansoor'
SITENAME = u"""<span style="color:black;">onCrash</span> <span style="color:darkblue;">=</span> <span style="color:#AA1032;">'reboot();'</span>"""
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
        'markdown.extensions.meta': {}
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
STATIC_PATHS = ['theme/images', 'images', 'extra/google3bc953001343abe6']
EXTRA_PATH_METADATA = {
     'extra/google3bc953001343abe6' : {'path': 'google3bc953001343abe6.html'}
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
TWITTER_USERNAME = u'talham_'
FEATURED_IMAGE = SITEURL + '/theme/images/apple-touch-icon-152x152.png'

# Legal
SITE_LICENSE = """Elegant theme documentation is licensed under a <a rel="license" 
    href="http://creativecommons.org/licenses/by/4.0/">
    Creative Commons Attribution 4.0 International License</a>.""" 


# SEO
SITE_DESCRIPTION = u'My name is Talha Mansoor \u2015 a software engineer who gets things done. I am talha131 at Github and @talham_ at twitter. I design and build software products for iOS and OSX. I work on Jump Desktop which is a remote desktop application for iOS, OSX and Android. This is my personal blog.'

# Landing Page
PROJECTS = [{'name': 'Elegant', 'url': 'http://oncrashreboot.com/pelican-elegant',
             'description': 'A clean and distraction free Pelican theme, with search and a lot more unique features. Built with Jinja2 and Bootstrap'},
            {'name': 'Logpad + Duration', 'url': 'https://github.com/talha131/logpad-plus-duration#logpad--duration',
             'description': 'Vim plugin to emulate Windows Notepad logging feature,'                        ' and log duration of each entry'},
            {'name': 'Pelican', 'url': 'https://github.com/getpelican/pelican/commits?author=talha131',
             'description': 'Static site generator that supports Markdown and reST syntax'},
            {'name': 'Pelican Plugins', 'url': 'https://github.com/getpelican/pelican-plugins/commits?author=talha131',
             'description': 'Bunch of plugins for Pelican blog engine'},
            {'name': 'Asana to Github Issues', 'url': 'https://github.com/talha131/AsanaToGithub#asana-to-github',
             'description': 'Command-line program to move your tasks from Asana projects to Github issues'},
            {'name': 'Asana', 'url': 'https://github.com/pandemicsyn/asana/commits?author=talha131',
             'description': 'Python Asana API bindings'},
            {'name': 'Ctags', 'url': 'https://github.com/fishman/ctags/commits?author=talha131',
             'description': 'Exuberant Ctags clone with ObjectiveC and CSS support'},
            {'name': 'Wasavi', 'url': 'https://github.com/akahuku/wasavi/commits?author=talha131',
             'description': 'A browser extension that changes textarea element to Vi editor'}]

LANDING_PAGE_ABOUT = {'title': 'I design and build software products for iOS and OSX',
                      'details': """<div itemscope itemtype="http://schema.org/Person"><p>My name
        is <span itemprop="name">Talha Mansoor</span>.
       I am <a href="https://github.com/talha131/" title="My Github
       profile" itemprop="url"><span itemprop="nickname">talha131</span></a> at Github and <a
       href="https://twitter.com/talham_/" title="My Twitter
       profile" itemprop="url">@talham_</a> at twitter. You can also reach me via <a
       href="mailto:talha131@gmail.com" title="My email
       address" itemprop="email">email</a>.</p><p>I work on <a href="http://jumpdesktop.com/"
       title="Jump Desktop" itemprop="affiliation">Jump Desktop</a> which is a remote desktop
       application for iOS, OSX and Android. I play a broad role there - which
       includes research, product design, engineering and deployment. I also
       lend a hand in user support.</p><p>I try to contribute to society by
       striving to create great software products that make people's lives
       easier. I believe software is the most effective way to touch others'
       lives in our day and time.</p><p>I mostly work in C, C++ and Objective-C
       on OSX and Linux, I also dabble in Python, Vim-L and JavaScript. I do not
       pigeonhole myself to specific languages or frameworks. A good developer
       is receptive and has the ability to learn new technologies. I also often
       contribute to open source projects and beta test startup
       products.</p><p>Besides programming, I <a
       href="https://www.fitocracy.com/profile/Andrew-Dufresne/" title="My
       Fitocracy profile" itemprop="url">exercise</a> and <a
       href="http://www.goodreads.com/talha131" title="My GoodReads
       profile" itemprop="url">read books</a> regularly. To be a stronger and better version of
       myself!</p><p>English is my second language. I am also learning <a
       href="http://www.duolingo.com/talha131" title="My Duolingo
       profile" itemprop="url">German from Duolingo</a>.</p></div>"""}
