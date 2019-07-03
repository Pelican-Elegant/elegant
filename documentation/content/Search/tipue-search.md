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
