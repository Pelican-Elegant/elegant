#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

# Important: Do not set SITEURL. It breaks deploy previews on Netlify
SITEURL = ''
RELATIVE_URLS = False

SOCIAL = (('Github', 'https://github.com/Pelican-Elegant/elegant'), ('RSS', SITEURL + '/feeds/all.atom.xml'))

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'

DELETE_OUTPUT_DIRECTORY = True
