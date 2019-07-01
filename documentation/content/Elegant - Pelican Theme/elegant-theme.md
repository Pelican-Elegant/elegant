Title: Elegant
Subtitle: Why it is the best Pelican theme
Date: 2013-08-27 23:20
Category: Elegant - Pelican Theme
Tags: jinja2, bootstrap, pelican-theme, font-awesome
Summary: Elegant is a minimal, stylish and responsive Pelican theme. Its unique features are search, Mailchimp, twitter card, and custom 404 page.
Slug: elegant-best-pelican-theme-features
comment_id: 2189d14-elegant-a-theme-for-pelican
modified: 2013-10-11 23:00
keywords: pelican theme, responsive theme, tipue search

[TOC]

What makes Elegant so special?

## Search

Static sites usually do not offer search. Elegant uses [Tipue
Search](http://www.tipue.com/search/)- an open source jQuery plugin, to offer
search for your static site.

There are two search modes.

1. **JSON Mode** Your site pages will be stored in JSON at your server. Tipue
   Search will use AJAX to access it and render search result. You need [Tipue
   Search plugin](https://github.com/getpelican/pelican-plugins) to use this
   mode.
1. **Live Mode Search** Tipue Search will fetch your site using Sitemap, index
   it and store it in the visitor's cache. This mode requires [Sitemap
   plugin](https://github.com/getpelican/pelican-plugins).

Use JSON mode if you value speed, or have a large site, or don't want to
overwhelm your host server for every search query.

Here is how the search result looks like

![Search result for App Store]({static}/images/elegant-theme_search-result.png)

Search box is part of main navigation menu so that visitor can search from any
page.

![Search box]({static}/images/elegant-theme_search-box.png)

## Custom 404 Page

Elegant has a custom Error 404 page for your readers.

![Error 404 page]({static}/images/elegant-theme_error-404-page.png)

---

## Elegant - Technical Nitty-Gritty

### License

The license requires that you give credit to me, Talha Mansoor, as the author
of the Elegant theme on every site that uses this theme. I have placed the
attribution in the footer of every page. Do not remove it. If you need to
remove or change the style of the attribution, please get in [touch with
me](http://oncrashreboot.com/#about-me) first.

Along with this attribution clause, Elegant theme is licensed under The MIT
License.

If you use my theme, I would love to hear from you. [Get in
touch](http://oncrashreboot.com/#about-me) and let me know about it. I may link
to your site too.

### Contribute

Front end design is not my strong suite. I must have made some blunders in this
design unknowingly. Please don't let me go away with buggy code.

- File bugs at [Github
  issues](https://github.com/Pelican-Elegant/elegant/issues)
- Share your ideas about the design in the comments below
- And most of all contribute improvements to [this
  project](https://github.com/Pelican-Elegant/elegant/)

There are two problem areas that I can think of,

1. Internet Explorer support
1. Web safe fonts. I developed this theme on a MacBook Retina. Although I have
   tried to make sure it looks great on all platforms but it still needs polish

Besides these, there must be other bugs that I haven't noticed yet. I need your
help to hunt them down and make them behave.
