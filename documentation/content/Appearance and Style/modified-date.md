Title: How does modified metadata works
Tags: web-design, meta-data, date
Category: Appearance & Style
Date: 2014-04-19 14:52
Slug: how-does-modified-metadata-works
Disqus_identifier: q4nz2k0-how-does-modified-metadata-works
Subtitle:
Summary: Use modified metadata to show the date at which you last updated the article
Keywords:

You need to update your articles time and again. Sometimes it makes sense to
display the date when you updated the article. You can show the last updated
date of the article by defining `modified` in your article metadata.

This is how it is displayed in the side bar,

![Modified Date]({static}/images/elegant-theme_last-modified.png)

Pelican post [version
3.3](https://github.com/getpelican/pelican/releases/tag/3.3.0) has a new
[`modified` metadata](https://github.com/getpelican/pelican/pull/1148). Type of
its value is `datetime`.

Depending on your
[`DATE_FORMATS`](http://docs.getpelican.com/en/latest/settings.html#basic-settings)
setting you can put modified date in your reST formated file as

    :::Rest
    :modified: 2014-01-22 14:30

Elegant will process it and display the last updated as "Jan 22, 2014".

Previous versions do not have `modified` metadata in which case type of its
value is string. If you are using old version of Pelican, i.e 3.3 or less, make
sure you assign it a value exactly the way you want it to appear. Taking the
example from above, metadata in your reST formated file should be,

    :::Rest
    :modified: Jan 22, 2014

You can also assign raw HTML to it. For example,

    :::html
    :modified: <a href="https://github.com/talha131/onCrashReboot/" title="Revision History">Aug 29, 2013</a>

But I do **not** recommend it because it will break on newer versions of
Pelican. In fact, you should ditch Pelican 3.3 or less and move to a higher
version if you require `modified` metadata.
