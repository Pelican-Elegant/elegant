#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

AUTHOR = "Pelican Elegant Team"
SITENAME = "Elegant Documentation"
SITEURL = ""

PATH = "content"

# Regional Settings
TIMEZONE = "Asia/Karachi"
DATE_FORMATS = {"en": "%b %d, %Y"}
DEFAULT_LANG = "en"

# Plugins and extensions
MARKDOWN = {
    "extension_configs": {
        "markdown.extensions.admonition": {},
        "markdown.extensions.codehilite": {"css_class": "highlight"},
        "markdown.extensions.extra": {},
        "markdown.extensions.meta": {},
        "markdown.extensions.toc": {"permalink": "true"},
    }
}

PLUGIN_PATHS = ["plugins"]
PLUGINS = [
    "sitemap",
    "extract_toc",
    "tipue_search",
    "liquid_tags.img",
    "neighbors",
    "render_math",
    "related_posts",
    "assets",
    "share_post",
    "series",
]
SITEMAP = {
    "format": "xml",
    "priorities": {"articles": 0.5, "indexes": 0.5, "pages": 0.5},
    "changefreqs": {"articles": "monthly", "indexes": "daily", "pages": "monthly"},
}

# Appearance
THEME = "themes/elegant"
TYPOGRIFY = True
DEFAULT_PAGINATION = False

# Defaults
DEFAULT_CATEGORY = "Miscellaneous"
USE_FOLDER_AS_CATEGORY = False
ARTICLE_URL = "{slug}"
PAGE_URL = "{slug}"
PAGE_SAVE_AS = "{slug}.html"

# Feeds
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
CATEGORY_FEED_ATOM = None
CATEGORY_FEED_RSS = None

# Social
SOCIAL = (
    ("Github", "https://github.com/Pelican-Elegant/"),
    ("RSS", SITEURL + "/feeds/all.atom.xml"),
)

CLAIM_GOOGLE = "Bk4Z5ucHLyPXqlZlj5LzANpYBBSvxqBW4E8i-Kwf-bQ"
CLAIM_BING = "8FF1B025212A47B5B27CC47163A042F0"

# Elegant theme
STATIC_PATHS = ["theme/images", "images", "extra/robots.txt"]
EXTRA_PATH_METADATA = {"extra/robots.txt": {"path": "robots.txt"}}
DIRECT_TEMPLATES = ("index", "tags", "categories", "archives", "search", "404")
TAG_SAVE_AS = ""
AUTHOR_SAVE_AS = ""
CATEGORY_SAVE_AS = ""
USE_SHORTCUT_ICONS = True

# Elegant Labels
SOCIAL_PROFILE_LABEL = "Stay in Touch"
RELATED_POSTS_LABEL = "Keep Reading"
SHARE_POST_INTRO = "Like this post? Share on:"
COMMENTS_INTRO = "So what do you think? Did I miss something? Is any part unclear? Leave your comments below."

# Mailchimp
EMAIL_SUBSCRIPTION_LABEL = "Get Monthly Updates"
EMAIL_FIELD_PLACEHOLDER = "Enter your email..."
SUBSCRIBE_BUTTON_TITLE = "Send me Free updates"
MAILCHIMP_FORM_ACTION = "empty"

# SMO
TWITTER_USERNAME = ""
FEATURED_IMAGE = SITEURL + "/theme/images/apple-touch-icon-152x152.png"

# Legal
SITE_LICENSE = """Elegant theme documentation is licensed under a <a rel="license" 
    href="http://creativecommons.org/licenses/by/4.0/">
    Creative Commons Attribution 4.0 International License</a>."""

# SEO
SITE_DESCRIPTION = "Documentation website for Pelican-Elegant theme originally created by Talha Mansoor"

# Landing Page
PROJECTS = [
    {
        "name": "Elegant",
        "url": "https://github.com/Pelican-Elegant/elegant",
        "description": "A clean and distraction free Pelican theme, with search and a lot more unique features. Built "
        "with Jinja2 and Bootstrap",
    },
    {
        "name": "Elegant Documentation",
        "url": "https://github.com/Pelican-Elegant/documentation",
        "description": "Documentation repository for Pelican-Elegant theme",
    },
]

LANDING_PAGE_ABOUT = {
    "title": "Live demonstration and documentation of Pelican-Elegant Theme",
    "details": """<p>This page serves both as documentation site and demonstration of Pelican-Elegant theme 
        capabilities and look&amp;feel.</p><p>Please do check our Project pages and browse this site for more information.
        </p>""",
}
