---
Title: How to use Google Analytics
Tags: web-analytics
Category: Analytics, SEO and SMO
Date: 2013-11-11 23:05
Slug: how-to-use-google-analytics
Comment_id: cf14ac5-how-to-use-google-analytics
Subtitle:
Summary: Elegant Pelican theme supports Google Analytics out of the box. This articles describes how to set it up.
Keywords:
authors: Talha Mansoor
---

Elegant supports the popular web tracking service,
[Google Analytics](http://www.google.com/analytics/).

[Get your property
ID](https://support.google.com/analytics/answer/1032385?hl=en) from your Google
Analytics account. It has this format `UA-XXXXX-X`.

Set `GOOGLE_ANALYTICS` variable to it in your configuration.

    :::python
    GOOGLE_ANALYTICS = u'UA-00000000-1'

That's it. Elegant will take care of the rest.
