#!/usr/bin/env python
# encoding: utf-8
# Copyright (C) 2017, 2018 Pablo Iranzo Gómez <Pablo.Iranzo@gmail.com>

import os
import re
import time

import setuptools

# In python < 2.7.4, a lazy loading of package `pbr` will break
# setuptools if some other modules registered functions in `atexit`.
# solution from: http://bugs.python.org/issue15881#msg170215

try:
    import multiprocessing  # noqa
except ImportError:
    pass

filename = 'setup.cfg'
regexp = '\Aversion.*([0-9]+)'

line = ""
with open(filename, 'r') as f:
    for line in f:
        if re.match(regexp, line):
            # Return earlier if match found
            break

version = line.split("=")[1].strip()
try:
    travis = os.environ['TRAVIS_JOB_ID']
except:
    travis = None

strings = time.strftime("%Y,%m,%d,%H,%M,%S")
t = strings.split(',')
numbers = [str(x) for x in t]

if travis:
    os.environ['PBR_VERSION'] = "%s.%s.%s" % (version, travis, "".join(numbers))
else:
    os.environ['PBR_VERSION'] = "%s.%s.%s" % (version, 0, "".join(numbers))

setuptools.setup(setup_requires=['pbr>=2.0.0'], pbr=True)

