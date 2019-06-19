#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = 'https://pelicanelegant.netlify.com'
RELATIVE_URLS = False
SOCIAL = (('Github', 'https://github.com/Pelican-Elegant/'), ('RSS', SITEURL + '/feeds/all.atom.xml'))

DELETE_OUTPUT_DIRECTORY = False
