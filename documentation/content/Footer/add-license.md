Title: Add License to your Site
Tags: nuances
Category: Footer
Date: 2014-04-22 16:23
Slug: add-license-to-your-site
Summary: You can display your preferred license in the footer

You can optionally define `SITE_LICENSE` variable in Pelican configuration. It will appear in the footer of the site.

For example,

```python
SITE_LICENSE = """Content licensed under <a rel="license"
    href="http://creativecommons.org/licenses/by/4.0/" target="_blank">
    Creative Commons Attribution 4.0 International License</a>."""
```

It appears as

![Site License Demonstration]({static}/images/elegant-theme_license.png)
