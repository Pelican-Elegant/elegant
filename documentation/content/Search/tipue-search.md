---
Title: Add Search to your Site
Tags: unique
Date: 2019-07-03 19:56
Slug: add-tipue-search
Summary: Elegant lets you add search to your static site
Category: Search
---

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

## Configuration

To enable search, you need to enable `tipue_search` plugin and add `search` to `DIRECT_TEMPLATES` in your pelican configuration

```python
PLUGINS = [tipue_search']
DIRECT_TEMPLATES = (('index', 'tags', 'categories','archives', 'search'))
```
