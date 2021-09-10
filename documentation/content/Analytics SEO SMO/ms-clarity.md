---
Title: How to use Microsoft Clarity
Tags: web-analytics
Category: Analytics, SEO and SMO
Date: 2021-01-25 20:05
Slug: how-to-use-Microsoft-clarity
Comment_id: cf14ac5-how-to-use-Microsoft-clarity
Subtitle:
Summary: Elegant Pelican theme supports Microsoft Clarity out of the box. This articles describes how to set it up.
Keywords:
authors: Talha Mansoor
---

Elegant supports the popular web tracking service,
[Microsoft Clarity](https://clarity.microsoft.com/).

[Get your property ID](https://clarity.microsoft.com/projects/), click on your property and either the URL or the script shown for installation will indicate something like `(window, document, "clarity", "script", "54yzatb1en");`

The `54yzatb1en` will be your property id

Set `MS_CLARITY` variable to it in your configuration.

    :::python
    MS_CLARITY = u'54yzatb1en'

This will load the required script for reporting automatically

That's it. Elegant will take care of the rest.
