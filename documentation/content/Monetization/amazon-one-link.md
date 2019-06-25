---
author: Pablo Iranzo Gómez (pablo.iranzo@gmail.com)
title: Amazon OneLink Support
tags: amazon, affiliates, income
layout: post
date: 2019-01-02 22:47:47 +0100
comments: true
category: Monetization
description:
slug: amazon-onelink
disqus_identifier: amazon-onelink
---

Elegant supports [Amazon OneLink](https://affiliate-program.amazon.com/onelink/), so that you may monetize your traffic using affiliate links.

Visit Amazon website and create your OneLink account. Amazon will provide you a code snippet similar to following,

```html
<div id="amzn-assoc-ad-$UUID"></div>
<script
  async
  src="//z-na.amazon-adsystem.com/widgets/onejs?MarketPlace=US&adInstanceId=$UUID"
></script>
```

Pay close attention to the `amzn-assoc-ad-` part. The value following it is your Amazon OneLink id.

In your pelican configuration, preferably in the file `publishconf.py`, set `AMAZON_ONELINK` to your Amazon OneLink id, for example,

```py
AMAZON_ONELINK = "b63a2115-85f7-43a9-b169-5f4c8c275655"
```

When the site is generated, `$UUID` in the snippet above is substituted with your id. Thus, ensuring that correct referral code is passed to the script.

Now, when international visitors of your site click on a link on your site to buy from Amazon, they are redirected to their local or nearest Amazon market place.
For example, original link (Python book):

This is an optional feature. If you do not set the variable then Amazon OneLink script is not added to the rendered output.

You, as a content creator, should be aware of GDPR or other regulations. We recommend you to seek consent from your readers to use the affiliate links on your site.
