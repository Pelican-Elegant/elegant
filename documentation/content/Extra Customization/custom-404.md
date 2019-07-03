---
Title: Custom 404 Page
Tags: unique
Date: 2019-07-03 20:07
Slug: custom-404-page
Summary: Elegant has a custom 404 page
Category: Extra Customization
---

Elegant has a custom Error 404 page for your readers.

![Error 404 page]({static}/images/elegant-theme_error-404-page.png)

To enable, add `404` to your `DIRECT_TEMPLATES` in pelican configuration.

```python
DIRECT_TEMPLATES = (('index', 'tags', 'categories','archives', '404'))
```
