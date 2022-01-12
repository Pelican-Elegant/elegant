---
Title: Configuring Menu Items
Tags: "pelican-theme, pelican-plugin, menu items"
Category: Components
Date: "2021-09-14 14:00"
Slug: configuring-menu-items
Comment_id: x4jitcv-configuring-menu-items
Subtitle: null
Summary: Elegant can be configured to provide custom menu items for the site.
Keywords: "menu items, configuration"
Authors: Pablo Iranzo Gómez
modified: "2021-09-14T13:07:03.797Z"
---

Pelican allows to configure via the `pelicanconf.py` configuration file the variable `MENUITEMS`

When no configuration is set, the Menu will show:

- Categories
- Tags
- Archives

Additionally Pages can also be shown if configured via the `DISPLAY_PAGES_ON_MENU` variable, but, if we wan to configure the default list from above, we can define the pages like:

```py
    MENUITEMS = [ ('Categories', "{{ SITEURL }}/{{ CATEGORIES_URL }}" ), ('Tags', "{{ SITEURL }}/{{ TAGS_URL }}"), ('Archives', "{{ SITEURL }}/{{ ARCHIVES_URL }}") ] %}
```

For example:

```py
    MENUITEMS = [ ('My Twitter', "https://twitter.com/meme" ), ('My tech blog', "https://example.com/tech") ] %}
```

And those new entries will appear instead of the default
