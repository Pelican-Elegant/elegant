---
Title: How to use GoatCounter
Tags: web-analytics
Category: Analytics, SEO and SMO
Date: 2013-11-11 23:05
Slug: how-to-use-goat-counter
Comment_id: cf14ac5-how-to-use-goat-counter
Subtitle:
Summary: Elegant Pelican theme supports Goat Counter out of the box. This articles describes how to set it up.
Keywords:
authors: Azzam S.A
---

Elegant supports the popular web tracking service,
[Goat Counter](https://www.goatcounter.com/).

Get your site code from your Goat Counter account. It has this format `sitecode`.goatcounter.com

Set `GOAT_COUNTER` variable to it in your configuration.

    :::python
    GOAT_COUNTER = u'awesome-blog'

That's it. Elegant will take care of the rest.
