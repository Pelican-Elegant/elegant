#!/bin/bash
echo "Changing branch to 'next'"
sed -i "s/rev: master/rev: next/g" peru.yaml

# Remove sitemap declaration
sed -i "s/Sitemap.*//g"   content/extra/robots.txt

# Disallow all robots
sed -i "s#Disallow.*#Disallow: /#g"   content/extra/robots.txt

sed -i "s#SITEURL.*#SITEURL = 'https://pelican-elegant.github.io/next/'#g" publishconf.py
