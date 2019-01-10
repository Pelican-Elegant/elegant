Title: Avoid Unnecessary HTTP Requests
Tags: pelican-theme, pelican-plugin, page-speed
Category: Supported Plugins
Date: 2014-03-24 14:09
Slug: avoid-unnecessary-http-requests
Disqus_identifier: hk9m5eq-avoid-unnecessary-http-requests
Subtitle:
Summary: Use Pelican assets plugin to improve your website load speed
Keywords:

Visitor's browser will make separate HTTP requests to fetch `elegent.css`,
`custom.css`, `pygments.css`, `admonition.css` and `tipuesearch.css`. These separate requests can
be avoided using [Pelican plugin
`assets`](https://github.com/getpelican/pelican-plugins/tree/master/assets).

Install the required packages

    :::bash
    pip install webassets cssmin

Then enable `assets` plugin in your configuration.

    :::python
    PLUGINS = ['assets']

This minor fix will improve the load speed of your website. All style
sheets will be merged and minified into one style sheet, `style.min.css`.

Compact CSS will save many bytes of data which in turn will improve page speed
and parse time.

# Hacking Elegant Source Code

If you add a new CSS file to the theme while developing the Elegant theme, you
will need to add it to the list of files that are automatically minified.

Find the file `templates/_includes/minify_css.html`. You will need to add your
new CSS file to Line 1, *before* `css/custom.css`.

We recommend you add custom CSS to `custom.css` for personal use. If you add to
`custom.css` you will not need to modify the `minify_css.html` file.
