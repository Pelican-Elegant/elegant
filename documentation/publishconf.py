#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys

sys.path.append(os.curdir)
from pelicanconf import *

# Important: Changing SITEURL may break links in deploy-previews
if os.environ.get("CONTEXT") == "production":
    SITEURL = "https://elegant.oncrashreboot.com"
    FEED_ALL_ATOM = "feeds/all.atom.xml"
    CATEGORY_FEED_ATOM = "feeds/{slug}.atom.xml"

    if os.environ.get("STAT_COUNTER_PROJECT_PROD") and os.environ.get(
        "STAT_COUNTER_SECURITY_PROD"
    ):
        STAT_COUNTER_PROJECT = os.environ.get("STAT_COUNTER_PROJECT_PROD")
        STAT_COUNTER_SECURITY = os.environ.get("STAT_COUNTER_SECURITY_PROD")
        GOOGLE_ANALYTICS = os.environ.get("GOOGLE_ANALYTICS_PROD")

elif os.environ.get("CONTEXT") == "branch-deploy" and os.environ.get("HEAD") == "next":
    SITENAME = "Elegant (Next)"
    SITESUBTITLE = "Pre Release Documentation of The Best Pelican Theme"
    SITEURL = "https://next.elegant.oncrashreboot.com"
    LANDING_PAGE_TITLE = "Elegant (Next) – Why it is the Best Pelican Theme"
    if os.environ.get("STAT_COUNTER_PROJECT_NEXT") and os.environ.get(
        "STAT_COUNTER_SECURITY_NEXT"
    ):
        STAT_COUNTER_PROJECT = os.environ.get("STAT_COUNTER_PROJECT_NEXT")
        STAT_COUNTER_SECURITY = os.environ.get("STAT_COUNTER_SECURITY_NEXT")
        GOOGLE_ANALYTICS = os.environ.get("GOOGLE_ANALYTICS_NEXT")

else:
    SITEURL = ""

RELATIVE_URLS = False

SOCIAL = (
    ("Github", "https://github.com/Pelican-Elegant/elegant"),
    ("RSS", SITEURL + "/feeds/all.atom.xml"),
)

DELETE_OUTPUT_DIRECTORY = True
