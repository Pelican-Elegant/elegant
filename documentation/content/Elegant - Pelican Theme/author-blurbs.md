Title: Adding Author Blurbs
Tags: pelican-theme, web-design
Category: Elegant - Pelican Theme
Date: 2018-12-07 11:00
Slug: adding-author-blurbs
Disqus_identifier: c8et6bu-adding-author-blurbs
Subtitle:
Summary: Adding informational author blurbs
Keywords:

[TOC]

## Adding Author Blurbs

At the end of each article, you can provide a small blurb about the author. This
can be done by setting up the `AUTHORS` dictionary in your configuration file.

    :::python
    AUTHORS = {
        u'Talha Mansoor': {
            u'blurb': """ created Elegant Pelican theme, dabbles in Python, Vim-L and JavaScript. They can be reached on Github, Twitter and email.""",
            u'url': 'https://github.com/talha131/'
        },
    }

Add an entry for each author you'd like a blurb to appear for.

These blurbs will appear for each known author, as defined in the `AUTHORS`
dictionary. If an unknown author appears, they will not receive a blurb.

The article author is determined by the provided metadata in your content
file. Valid values are:

- `author:` - This defines the _single_ author of the article.
- `authors:` - This is a comma separated list of all article authors. Each known author will get a blurb. Each unknown author will not get a blurb.
- Default author defined in your configuration file. If either of the two metatags above are not used, the default author you configured will be utilized. This author still requires an entry in the `AUTHORS` dictionary.

**Note:** If you define multiple authors, but use the `author:` metatag, a blurb
will not be generated. This metatag is for a _single_ author. The correct way to
declare more than one author is to use `authors:`.

This is an example of multiple authors using the following metatag value:

    :::python
    authors: Talha Mansoor, Milton Bradley

![Author Blurb]({static}/images/author-blurb.png)
