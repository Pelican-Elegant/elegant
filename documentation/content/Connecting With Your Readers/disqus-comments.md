---
Title: Comments -- Enable Disqus
Tags: interaction
Category: Connecting With Your Readers
Date: 2014-04-21 16:39
Slug: enable-disqus-comments
comment_id: 9jgwmy8-how-to-use-disqus-comments-elegantly
Summary: Elegant offers Disqus comments out of the box with few unique features
authors: Talha Mansoor
comment_id: aa8pfjdv5f
disqus_filter: off
---

You can use Disqus for comments. You have to set `DISQUS_SITENAME` to Disqus
site name identifier in configuration to enable comments.

That's it. Elegant will take care of the rest.

You can see a working example of Disqus comments in this article.

## Show Disqus comments by default

Just set `DISQUS_SITENAME` variable.

## Hide Disqus comments by default

Unset `DISQUS_SITENAME` variable.

This is the default setting.

## Hide Disqus comments by default. Show on Selected

1. Set `DISQUS_SITENAME`
1. Set `DISQUS_FILTER` to `True`

This will hide Disqus form on all pages.

Now to show Disqus form on selected posts, in article metadata set

```yaml
disqus_filter: off
```

## Show Disqus comments by default. Hide on Selected

1. Set `DISQUS_SITENAME`
1. Remove `DISQUS_FILTER` or set it to `False` which is its default value

This will hide Disqus form on all pages.

Now to hide Disqus form on selected posts, in article metadata set

```yaml
disqus_filter: on
```
