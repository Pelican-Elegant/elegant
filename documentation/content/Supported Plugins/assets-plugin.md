Title: How To Improve the Download Time For Your Pages
Tags: pelican-theme, pelican-plugin, page-speed
Category: Supported Plugins
Date: 2014-03-24 14:09
Slug: avoid-unnecessary-http-requests
Comment_id: hk9m5eq-avoid-unnecessary-http-requests
Subtitle:
Summary: Pelican can be configured to compile multiple assets for your website into one single asset. When these assets are combined together, they are reduce to only their necessary components, and can be fetch by the webpage in a single call.
Keywords:
Authors: Talha Mansoor, Jack De Winter

When a webpage is created, webpage authors and static page generators will often grab
low-level asset files from a trusted location. Between Pelican and Elegant, these files will
often number between 8 and 15 CSS or JavaScript files[^css-javascript]. While these files are
essential to the proper look and feel of a properly designed website, the overhead of this
content being in separate files is that one request is made from the browser to the webserver
for each file.

[^css-javascript]: If you would like to learn more about these, [W3Schools](https://www.w3schools.com/) have some great introductions to these files and their affects. The important part about these files is that they change how the browser displays and reacts to a given webpage. These files are use on 99.9% of the websites in existence due to their versatility.

Pelican provides a plugin that takes the various CSS and JavaScript files and compiles each
group of them into a single file. Not only does this process reduce the number of calls to
retrieve files from the webserver, but it minifies[^minifies] or reduces the overall size of
those files as well.

[^]: [Wikipedia](<https://en.wikipedia.org/wiki/Minification_(programming)>) has a good article on minification. The summary is that anything unnecessary over a series of files is removed and concatenated together to produce a single file that is the minimum size possible while not losing any understandability.

## Configuration

To enable Asset Management for your website, add `assets` to `PLUGINS` in your Pelican
configuration.

```python
PLUGINS = ['assets']
```

Note that these values must be added to any existing values present for the `PLUGINS`
configuration variables.

!!! note
The [assets plugin](https://github.com/getpelican/pelican-plugins/blob/master/assets/Readme.rst) requires the Python `webassets` and `cssmin` packages to be installed.

## Debugging Notes

Note that you will not see the full power of the Assets Management plugin if you are working in
debug mode, that is building the website while using `--debug` on the Pelican command line.
In debug mode, some of the files may be minified into the `style.min.css` file, but the
original files will be included in the HTML page they are referenced from.

This will look something like the following:

```html
<link
  rel="stylesheet"
  href="http://localhost:8000/theme/webassets-external/f89ba5f14545a8fa0e81c1c6e2b5fc13_pygments.css"
/>
<link
  rel="stylesheet"
  href="http://localhost:8000/theme/webassets-external/96b04e88b0ba11363f4f2e2f59b5fb18_tipuesearch.css"
/>
<link
  rel="stylesheet"
  href="http://localhost:8000/theme/webassets-external/9c80344d72edcf2ebb95daecd6dfa24c_elegant.css"
/>
<link
  rel="stylesheet"
  href="http://localhost:8000/theme/webassets-external/d8877b08872b9883b67fbef219dfdebb_admonition.css"
/>
<link
  rel="stylesheet"
  href="http://localhost:8000/theme/webassets-external/78ddd4ea7393d1ac1fd9f91c21aa8b5f_custom.css"
/>
```

When the `--debug` command line option is removed, the lines described above will be
replaced with a line like:

```html
<link
  rel="stylesheet"
  href="https://jackdewinter.github.io/theme/css/style.min.css?c4027515"
/>
```

## Improving Elegant

If you are developing a new feature (for the theme or for your own website), you may need to
add a new CSS file to make sure that it renders properly on the webpage. Elegant ships with
the ability support minification of CSS files through the `minify_css.html` file. This file
is located in the `templates/_includes` directory of the theme and has the following
contents:

```text
{% assets filters="cssmin", output="css/style.min.css", "css/pygments.css", "tipuesearch/tipuesearch.css","css/elegant.css", "css/admonition.css", "css/custom.css" %}
<link rel="stylesheet" href="{{ SITEURL }}/{{ ASSET_URL }}">
{% endassets %}
```

To ensure that your new CSS file is minified, we advise you to follow one of these two
suggestions.

If you are planning to add a new feature to your own website, consider placing the changes in
the Elegant theme's `custom.css` file. This file is also located in the `templates/_includes`
directory, and is blank in a standard Elegant theme. As the `custom.css` file is already in
the list of files to minify, no addition modifications are required. If you are not sure
whether or not the feature will be submitted as part of Elegant, this is a good place to
start at.

If you are planning to add a new feature to Elegant and share it with others, you will be asked
to place any CSS changes for your feature in a new CSS file. This new file should be saved in
the theme's `templates/_includes` directory with the other CSS files. To ensure that the new
file is minified, a reference to it must be added to the first line of the `minify_css.html`
file, after the `css/admonition.css` file reference and before the `css/custom.css` file
reference.
