---
authors: Pablo Iranzo Gómez, Talha Mansoor
title: Amazon OneLink Support
tags: amazon, affiliates, income
date: 2019-01-02 22:47:47 +0100
comments: true
category: Monetizing Your Blog
description:
slug: amazon-onelink
comment_id: amazon-onelink
---

Elegant supports [Amazon OneLink](https://affiliate-program.amazon.com/onelink/), so that you may monetize your traffic using affiliate links.

With the recent changes to Amazon, linking your sites on the Amazon US site and putting a link to it, will automatically redirect to the closes Amazon site of visitor, rendering the JavaScript code used in the past obsolete.

As the links for the previous feature required to be one, there's no migration needed except removing the old setting `AMAZON_ONELINK` from your pelicanconf.py from now on. If you leave the setting it might be useful for you as it will show automatically the following footer:

You, as a content creator, should be aware of GDPR or other regulations.
[Section 5 of the Operating
Agreement](https://affiliate-program.amazon.com/help/operating/agreement) for
Amazon Associates states that you need to disclose your affiliation with Amazon and that you earn from qualifying purchases.

To conform to this rule in the agreement, Elegant automatically adds the disclaimer in the footer of the website if `AMAZON_ONELINK` variable is set. It looks like this,

![Amazon OneLink Disclosure]({static}/images/amazon-online-disclaimer.png)
