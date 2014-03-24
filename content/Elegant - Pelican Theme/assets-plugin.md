Title: Avoid Unnecessary HTTP Requests
Tags: pelican-theme
Category: Elegant - Pelican Theme
Date: 2014-03-24 14:09
Slug: avoid-unnecessary-http-requests
Disqus_identifier: hk9m5eq-avoid-unnecessary-http-requests
Subtitle: 
Summary: Use Pelican assets plugin to improve your website load speed 
Keywords: 

Visitor's browser will make separate HTTP requests to fetch `elegent.css`,
`custom.css`, `pygments.css` and `tipuesearch.css`. These four separate
requests can be avoided using [Pelican plugin
`assets`](https://github.com/getpelican/pelican-plugins/tree/master/assets).

Install the required packages

    :::bash
    pip install webassets cssmin

Then enable `assets` plugin in your configuration.

    :::python
    PLUGINS = ['assets']

This minor fix will improve the load speed of your website. All four style
sheets will be merged and minified into one style sheet, `style.min.css`.

Compact CSS will save many bytes of data which in turn will improve page speed
and parse time.

