Title: How do I set Favicon and Speed Dial icon of my blog
Tags: favicon
Category: Elegant - Pelican Theme
Date: 2013-11-08 22:42
Slug: how-do-i-set-favicons-and-speed-dial-icons
Disqus_identifier: p34md6k-how-do-i-set-favicons-and-speed-dial-icons
Subtitle: 
Summary: Elegant Pelican theme supports favicon and speed dial icon for Pelican
    blogs. This article describes how to set up this feature.
Keywords: 

Elegant supports favicon, Apple launcher icon and Opera speed dial icon. These
are disabled by default to avoid unnecessary HTTP requests on sites that do not
use them.

To enable set `USE_FAVICON` in your configuration

    :::python
    USE_FAVICON = True

Place your images in `content/theme/images` directory, and define `STATIC_PATHS`
variable in your configuration

    :::python
    STATIC_PATHS = ['theme/images', 'images']

Your images should have these names,

1. `apple-touch-icon-114x114.png`
1. `apple-touch-icon-144x144.png`
1. `apple-touch-icon-57x57.png`
1. `apple-touch-icon-72x72.png`
1. `apple-touch-icon.png`
1. `favicon.ico`

I recommend using [Iconifier.net](http://iconifier.net/) to generate the set of
images.

