#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os

AUTHOR = "Elegant Team"
SITENAME = "Elegant"
SITESUBTITLE = "The Best Pelican Theme"
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
THEME = "../"
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

CLAIM_BING = "BC16AEBED17872F083B3E1E7A67454BD"

# Elegant theme
STATIC_PATHS = ["theme/images", "images", "extra/_redirects"]
EXTRA_PATH_METADATA = {"extra/_redirects": {"path": "_redirects"}}

if os.environ.get("CONTEXT") == "production":
    STATIC_PATHS.append("extra/robots.txt")
    EXTRA_PATH_METADATA["extra/robots.txt"] = {"path": "robots.txt"}
else:
    STATIC_PATHS.append("extra/robots_deny.txt")
    EXTRA_PATH_METADATA["extra/robots_deny.txt"] = {"path": "robots.txt"}

DIRECT_TEMPLATES = ["index", "tags", "categories", "archives", "search", "404"]
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
SITE_LICENSE = """Content licensed under <a rel="license"
    href="http://creativecommons.org/licenses/by/4.0/" target="_blank">
    Creative Commons Attribution 4.0 International License</a>."""
HOSTED_ON = {"name": "Netlify", "url": "https://www.netlify.com/"}

# SEO
SITE_DESCRIPTION = (
    "Documentation of Elegant, a theme for Pelican, originally created by Talha Mansoor"
)

# Landing Page
PROJECTS_TITLE = "Related Projects"
PROJECTS = [
    {
        "name": "Elegant",
        "url": "https://github.com/Pelican-Elegant/elegant",
        "description": "Source code of Elegant theme",
    },
    {
        "name": "Issue Tracker",
        "url": "https://github.com/Pelican-Elegant/elegant/issues",
        "description": "Give your feedback, ask questions or report issues",
    },
    {
        "name": "Roadmap",
        "url": "https://github.com/Pelican-Elegant/elegant/milestones",
        "description": "See planned features and estimated release dates",
    },
    {
        "name": "Press Kit",
        "url": "https://github.com/Pelican-Elegant/elegant/tree/master/elegant-logo",
        "description": "Writing an article on Elegant? Get Elegant logo from here",
    },
    {
        "name": "onCrashReboot",
        "url": "https://www.oncrashreboot.com/",
        "description": "Home page of Elegant creator and lead developer",
    },
    {
        "name": "Pelican",
        "url": "https://github.com/getpelican/pelican/",
        "description": "Static site generator that powers Elegant",
    },
    {
        "name": "Pelican Plugins",
        "url": "https://github.com/getpelican/pelican-plugins",
        "description": "Collection of plugins for the Pelican static site generator",
    },
]

LANDING_PAGE_TITLE = "Elegant – Why it is the Best Pelican Theme"

AUTHORS = {
    "Talha Mansoor": {
        "url": "https://www.oncrashreboot.com/",
        "blurb": "is the creator and lead developer of Elegant theme.",
        "avatar": "/images/avatars/talha131.png",
    },
    "Pablo Iranzo Gómez": {
        "url": "http://iranzo.github.io",
        "blurb": " opensource enthusiast and Lego fan doing some python simple programs like @redken_bot in telegram, etc",
        "avatar": "https://avatars.githubusercontent.com/u/312463",
    },
    "Jack De Winter": {
        "url": "http://jackdewinter.github.io",
        "blurb": "ever evolving, ever learning",
    },
    "Matija Šuklje": {
        "url": "https://matija.suklje.name",
        "blurb": "FOSS lawyer by trade, hacker by heart.",
    },
}
