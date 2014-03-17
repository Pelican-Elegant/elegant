Title: How to show RSS feeds icon
Tags: pelican-theme, rss
Category: Elegant - Pelican Theme
Date: 2014-03-17 15:28
Slug: how-to-show-rss-feeds-icon
Disqus_identifier: ijvxwtg-how-to-show-rss-feeds-icon
Subtitle: 
Summary: Elegant supports RSS and Atom feeds for your posts, categories and tags
Keywords: 

RSS feeds is the oldest and arguably the most used format to publish blog
updates. Its use is not limited to RSS aggregators and readers. Tools like
[IFTTT](https://ifttt.com/recipes?channel=feed) and
[Calibre](http://manual.calibre-ebook.com/news.html) increases RSS feeds' power
and versatility by manifolds.

To enable RSS feeds, see [Feed
Settings](http://docs.getpelican.com/en/latest/settings.html#feed-settings) in
Pelican documentation.

Links to RSS feeds are embedded in every page. Links to category and tag
feeds are embedded only in the Categories and Tags pages respectively.

Elegant does not show RSS feeds icon out of the box, though it can be easily
enabled.

All RSS consumers have the ability to capture feed links from a web address.
For example, you need not put `http://oncrashreboot.com/feeds/all.atom.xml` in
your RSS reader. Just `http://oncrashreboot.com` is enough. Your reader should
be able to extract feed URL from the link.

All popular browsers can detect RSS feeds on the page and show a visual cue. In
Firefox, you can add "Subscribe" button to the
[toolbar](https://support.mozilla.org/en-US/kb/customize-firefox-controls-buttons-and-toolbars?redirectlocale=en-US&redirectslug=How+to+customize+the+toolbar).
For Chrome, you can use [RSS Subscription
Extension](https://chrome.google.com/webstore/detail/rss-subscription-extensio/nlbjncdgjeocebhnmkbbbdekmmmcbfjd).

Here is an example of my category feeds in Chrome.

![Display RSS Feeds in Chrome](|filename|/images/rss-feeds-chrome-category-feeds.png)

These options make it redundant to have a separate RSS icon on the page.
Elegant is all about a clean and minimal UI.

But it is not so hard to enable it. First [configure the Social
widget](how-to-display-your-social-media-profiles). Then add a tuple for RSS,

    :::python

    SOCIAL = (('RSS', 'http://oncrashreboot.com/feeds/all.atom.xml'),)

Viola! You got yourself the RSS icon.

![RSS Feeds icon in Social widget](|filename|/images/rss-feeds-icon-social-widget.png)
