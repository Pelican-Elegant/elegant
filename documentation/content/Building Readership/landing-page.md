---
Title: Customize Home Page
Tags: nuances, remarkable, unique
layout: post
Date: 2019-07-01 01:22
comments: false
Slug: customize-home-page
Category: Building Readership
---

This is the page that visitors see when they open your website. Your chance to
make a good and lasting first impression. Most sites just display a list of
recent posts. Elegant goes the extra mile. Check this out

![Home Page Sample]({static}/images/elegant-theme_home-page-features.png)

You can see two sections here,

1. About me
1. My Projects

There is a third section below these two sections, "Recent articles"

![Recent Articles Section]({static}/images/elegant-theme_recent-posts.png)

## Welcome Heading

Define `LANDING_PAGE_TITLE` in your Pelican configuration. It will be displayed as the welcome heading. For example,

```python
LANDING_PAGE_TITLE = "Elegant – Why it is the Best Pelican Theme"
```

## About Me

To write about me section, create a page. See [Pelican documentation](http://docs.getpelican.com/en/stable/content.html#pages) on how to create a page.

The slug of the page should be `landing-page-about-hidden` and `status` should be `hidden`. Example,

```yaml
---
author: Talha Mansoor
title: What Is Elegant
layout: page
date: 2019-01-14 7:30:47 +0100
status: hidden
slug: landing-page-about-hidden
---

```

The content of this will become your "About me" section, and title will become the heading. You can write content in any markup language, like Markdown, AsciiDoc or reST, as long as Pelican has supports it.

### Deprecated

!!! Danger "Warning: Legacy Variable"

    `LANDING_PAGE_ABOUT` was available in Elegant V2.5.0. It has since been passed out in favour of `landing-page-about-hidden`. The new method lets you write "About Me" in your favourite markup language.

You can write up your own About me section using `LANDING_PAGE_ABOUT` variable
in your configuration. It is a dictionary that has two keys `title` and
`details`.

Value of `title` is displayed in the header of the home page, like
in the above example it is "I design and build software products for iOS and
OSX".

`details` is the text that appears under "About me" heading. You can add raw HTML to it.

## Projects

Projects list is read from `PROJECTS`. It is an array of dictionaries. Each
dictionary has three keys, `name` which will have name of your project, `url`
which will have URL of the project, and `description` which will have the
description of the project. You can define as many projects as you want. Here
is an example,

    #!Python
    PROJECTS = [{
        'name': 'Logpad + Duration',
        'url': 'https://github.com/talha131/logpad-plus-duration#logpad--duration',
        'description': 'Vim plugin to emulate Windows Notepad logging feature,'
        ' and log duration of each entry'},
        {'name': 'Elegant Theme for Pelican',
        'url': 'http://oncrashreboot.com/pelican-elegant',
        'description': 'A clean and distraction free theme, with search and a'
        ' lot more unique features, using Jinja2 and Bootstrap'}]

### Recent Articles

Recent articles show last `RECENT_ARTICLES_COUNT` whose default value is 10. It
also has a link to "all posts".
