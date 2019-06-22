---
author: Pablo Iranzo Gómez (pablo.iranzo@gmail.com)
title: Amazon onelink support
tags: amazon, affiliates, income
layout: post
date: 2019-01-02 22:47:47 +0100
comments: true
category: Monetization
description:
slug: amazon-onelink
disqus_identifier: amazon-onelink
---

Elegant has included support for [Amazon OneLink](https://affiliate-program.amazon.com/onelink/).

Amazon allows to define, on each 'store' for countries a tag used for referring the products shopped via the links to provide incomes/revenue to website/blog owners.

In order to maximize revenue, several shops for each country should be used, but only one link can be done for each one.

They provided a feature called 'OneLink' available from the US site that allows, via javascript code, to convert he links with referral included in a webpage to the ones relevant for the user's store, so user in 'US' will get a link to 'US' referral for the site owner, and one from 'FR' will get a link to amazon.fr with owner's referral.

Please, do check Amazon link above for more information.

About how Elegant simplifies the usage...

Amazon will provde you some code like below:

```html
<div id="amzn-assoc-ad-$UUID"></div>
<script
  async
  src="//z-na.amazon-adsystem.com/widgets/onejs?MarketPlace=US&adInstanceId=$UUID"
></script>
```

In order to use it, set in your `pelicanconf.py` the variable `AMAZON_ONELINK`, for example:

```py
AMAZON_ONELINK = "b63a2115-85f7-43a9-b169-5f4c8c275655"
```

When the site is generated, the script will substitute UUID for the above variable value and proper script will be loaded to redirect your visitors.

For example, original link (Python book):

- [US](https://amzn.to/2RvipYp)

Gets translated by OneLink to:

- [Canada](https://www.amazon.ca/dp/1449355730?s=books&ie=UTF8&qid=1546637046&sr=1-3&keywords=python&linkCode=sl1&linkId=34c3dec8f666e20197aa4674f8cbbe58&tag=iranzo0e-20)
- [France](https://www.amazon.fr/dp/1449355730?s=books&ie=UTF8&qid=1546637046&sr=1-3&keywords=python&linkCode=sl1&linkId=34c3dec8f666e20197aa4674f8cbbe58&tag=iranzo03-21)
- [Germany](https://www.amazon.de/dp/1449355730?s=books&ie=UTF8&qid=1546637046&sr=1-3&keywords=python&linkCode=sl1&linkId=34c3dec8f666e20197aa4674f8cbbe58&tag=iranzo06-21)
- [Italy](https://www.amazon.it/dp/1449355730?s=books&ie=UTF8&qid=1546637046&sr=1-3&keywords=python&linkCode=sl1&linkId=34c3dec8f666e20197aa4674f8cbbe58&tag=iranzo04-21)
- [Spain](https://www.amazon.es/dp/1449355730?s=books&ie=UTF8&qid=1546637046&sr=1-3&keywords=python&linkCode=sl1&linkId=34c3dec8f666e20197aa4674f8cbbe58&tag=iranzo-21)
- [UK](https://www.amazon.co.uk/dp/1449355730?s=books&ie=UTF8&qid=1546637046&sr=1-3&keywords=python&linkCode=sl1&linkId=34c3dec8f666e20197aa4674f8cbbe58&tag=iranzo0f-21)

Of course, if unset, no script load is instructed (nor present on the rendered pages) similar to what happens with piwik, google analytics, etc.

We assume that you, as a content creator, are aware of GDPR or other regulations, and expect you to seek consent from your readers to use these plugins.
