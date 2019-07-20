Title: How to use Multi Part plugin
Tags: pelican-theme, pelican-plugin, navigation, web-design
Category: Supported Plugins
Date: 2014-04-20 18:18
Slug: how-to-use-multi-part-plugin
Comment_id: 3ws2xke-how-to-use-multi-part-plugin
Subtitle:
Summary: Elegant integrates with Multi Part plugin out of the box
Keywords:

[Multi
parts](https://github.com/getpelican/pelican-plugins/tree/master/multi_part) is
a useful plugin that lets you write "multi-part" articles.

To mark articles that belong to the same series, define `parts` metadata.

    :::rest
    :parts: iCloud 101 Series

Elegant shows the multi-part series in the sidebar.

![multi-part example in the
sidebar]({static}/images/elegant-theme_multi-part-sidebar.png)

Articles are sorted by their date in ascending order. The oldest article is
considered "Part 1" and so on.

The currently opened article is displayed in italics. In the above example,
"Part 2" is opened in the browser tab.

Title attribute of HTML anchor tag `<a>` is set for each "Part" to its article
title; it is displayed when user hovers over the link.

![multi-part example with title of the
links]({static}/images/elegant-theme_multi-part-title-attribute.png)

As all other features, Elegant has some tricks up its sleeve.

## Series Title

By default Elegant uses value of `parts` as the title of the series. You can
define series title for your multi-part articles series. Define `series_title`
in your articles metadata, like,

    :::rest
    :parts: iCloud 101 Series
    :series_title: iCloud for Dummies

And this will give you,

![multi-part example with custom series title]({static}/images/elegant-theme_multi-part-custom-label.png)

You have to make sure `series_title` metadata is set for every article in the
series.

You can also define `SERIES_TITLE` in your Pelican configuration to set a
default value for `multi_part` widget label.

Elegant first looks for `SERIES_TITLE` in configuration, then `series_title` in
the article metadata, then `parts` metadata which it uses as the last resort.

I recommend you to let Elegant use `parts` instead of `series_title` and
`SERIES_TITLE`.

With `series_title` you will have to deal with the hassle of making sure all
articles in the series have it, which you are already doing for `parts`. So why
double the hassle?

With `SERIES_TITLE` you won't be able to have custom titles for the series'.
