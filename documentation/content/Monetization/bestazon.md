---
authors: Pablo Iranzo Gómez
title: Bestazon Support
tags: amazon, affiliates, income, bestazon
layout: post
date: 2019-01-12 07:30:47 +0100
comments: true
category: Monetization
description:
slug: amazon-bestazon
comment_id: amazon-bestazon
---

Elegant supports [BestAzon](https://bestazon.io/), so that you may monetize your traffic using affiliate links from amazon.

Similar to [Amazon One Link]({filename}amazon-one-link.md), bestazon provides technology that redirects amazon links to each country shop by using your associate tags

In order to configure Bestazon, an array should be provided containing variables for configuration, like:

```js
var BestAzon_Configuration = {
  Amzn_AfiliateID_US: "redken01-20",
  Amzn_AfiliateID_CA: "redken03-20",
  Amzn_AfiliateID_GB: "redken01-21",
  Amzn_AfiliateID_DE: "redken06-21",
  Amzn_AfiliateID_FR: "redken07-21",
  Amzn_AfiliateID_ES: "redken-21",
  Amzn_AfiliateID_IT: "redken0d-21",
  Amzn_AfiliateID_JP: "",
  Amzn_AfiliateID_IN: "",
  Amzn_AfiliateID_CN: "",
  Amzn_AfiliateID_MX: "",
  Amzn_AfiliateID_BR: "",
  Conf_Custom_Class: " BestAzon_Amazon_Link ", //enter if you'll like to add any CSS class to the Amazon links (can be used for styling)
  Conf_New_Window: "1", //enter "1" if you'll like to open Amazon links in new window (recommended), "2" to force open in the same window, keep blank if you'd use the defaults
  Conf_Link_Follow: "1", //enter "1" if you'll like to add no-follow to the Amazon links (recommended), "2" to not add no-follow
  Conf_Product_Link: "1", //enter "1" if you'll like to redirect international visitors to equivalent search page on local Amazon stores (recommended and fast), "2" if you want them to go to equiavalent product page (slow)
  Conf_Tracking: "1", //enter "1" if you'll like to enable tracking (useful to optimize the service to you), "2" to disable
  Conf_Footer: "1", //enter "1" to add credit in footer (recommended), "2" to disable
  Conf_Link_Keywords: "", //enter additional keywords - if any of these keywords is found in any URL on your site, that will be sent to Bestazon for localization (useful if you use short links like bitly to hide your affiliate links). E.g. enter "/amazon/" if all your Amazon links containt the string /amazon/
  Conf_Hide_Redirect_Link: "1", //enter "1" to not replace your original link with bestazon links (recommended), "2" if you want to replace (not recommended)
  Conf_Source: "BestAzonScript" //DO NOT CHANGE THIS
};
```

Follow <https://bestazon.io> to generate that configuration based on your tag id's first.

Elegant does take care of loading the script for BestAzon and inserting your configuration if defined.

In order to do so, in your pelican configuration, preferably in the file `publishconf.py`, set `AMAZON_BESTAZON` to your bestazon configuration, for example:

```py
AMAZON_BESTAZON = """var BestAzon_Configuration = {
"Amzn_AfiliateID_US": "redken01-20",
"Amzn_AfiliateID_CA": "redken03-20",
"Amzn_AfiliateID_GB": "redken01-21",
"Amzn_AfiliateID_DE": "redken06-21",
"Amzn_AfiliateID_FR": "redken07-21",
"Amzn_AfiliateID_ES": "redken-21",
"Amzn_AfiliateID_IT": "redken0d-21",
"Amzn_AfiliateID_JP": "",
"Amzn_AfiliateID_IN": "",
"Amzn_AfiliateID_CN": "",
"Amzn_AfiliateID_MX": "",
"Amzn_AfiliateID_BR": "",
"Conf_Custom_Class": " BestAzon_Amazon_Link ", //enter if you'll like to add any CSS class to the Amazon links (can be used for styling)
"Conf_New_Window": "1", //enter "1" if you'll like to open Amazon links in new window (recommended), "2" to force open in the same window, keep blank if you'd use the defaults
"Conf_Link_Follow": "1", //enter "1" if you'll like to add no-follow to the Amazon links (recommended), "2" to not add no-follow
"Conf_Product_Link": "1", //enter "1" if you'll like to redirect international visitors to equivalent search page on local Amazon stores (recommended and fast), "2" if you want them to go to equiavalent product page (slow)
"Conf_Tracking": "1", //enter "1" if you'll like to enable tracking (useful to optimize the service to you), "2" to disable
"Conf_Footer": "1", //enter "1" to add credit in footer (recommended), "2" to disable
"Conf_Link_Keywords": "", //enter additional keywords - if any of these keywords is found in any URL on your site, that will be sent to Bestazon for localization (useful if you use short links like bitly to hide your affiliate links). E.g. enter "/amazon/" if all your Amazon links containt the string /amazon/
"Conf_Hide_Redirect_Link": "1", //enter "1" to not replace your original link with bestazon links (recommended), "2" if you want to replace (not recommended)
"Conf_Source": "BestAzonScript" //DO NOT CHANGE THIS
};
"""
```

When the site is generated, if this variable is defined, it will load the configuration in `base.html` and load the script from bestazon that enables the link substituon.

Now, when international visitors of your site click on a link on your site to buy from Amazon, they are redirected to their local or nearest Amazon market place.

This is an optional feature. If you do not set the variable then BestAzon script is not added to the rendered output.

You, as a content creator, should be aware of GDPR or other regulations.
[Section 5 of the Operating
Agreement](https://affiliate-program.amazon.com/help/operating/agreement) for
Amazon Associates states that you need to disclose your affiliation with Amazon and that you earn from qualifying purchases.

To conform to this rule in the agreement, Elegant automatically adds the disclaimer in the footer of the website if `AMAZON_ONELINK` variable is set. It looks like this,

![Amazon OneLink Disclosure]({static}/images/amazon-online-disclaimer.png)
