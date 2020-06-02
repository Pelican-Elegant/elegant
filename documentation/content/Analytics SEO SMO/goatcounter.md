---
Title: How to use GoatCounter
Tags: web-analytics
Category: Analytics, SEO and SMO
Date: 2013-11-11 23:05
Slug: how-to-use-goatcounter
Comment_id: cf14ac5-how-to-use-goatcounter
Subtitle:
Summary: Elegant Pelican theme supports GoatCounter out of the box. This articles describes how to set it up.
Keywords:
authors: Azzam S.A
---

Elegant supports the popular web tracking service,
[GoatCounter](https://www.goatcounter.com/).

Get your integration endpoint from your GoatCounter account; it's listed at the top of the "site code" documentation.

Set `GOATCOUNTER` variable to it in your configuration:

    :::python
    GOATCOUNTER = u'http://example.goatcounter.com/count'

This will work for goatcounter.com hosted instances and self-hosted instances.

That's it. Elegant will take care of the rest.
