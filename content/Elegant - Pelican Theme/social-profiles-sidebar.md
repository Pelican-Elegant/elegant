Title: How to display your Social Media Profiles
Tags: pelican-theme, font-awesome
Category: Elegant - Pelican Theme
Date: 2014-01-27 00:28
Slug: how-to-display-your-social-media-profiles
Disqus_identifier: k7fpj4y-how-to-display-your-social-media-profiles
Subtitle: 
Summary: Elegant displays links to your social media profiles in sidebar in a customizable manner
Keywords:

Almost every Internet user has more than one social media profile on the
web. Bloggers use different sites to connect with their readers, create
a following, and engage in discussion with them.

Elegant lets you display links to your social media profiles in the
sidebar.

<img class="align-right" style="width: 262.0px; height: 140.0px;"
src="|filename|/images/social-profiles-sidebar-default.png" alt="Social
Profiles in the Sidebar" />

Each icon is a link to your social profile with an appropriate title
attribute. Elegant uses scalable vector icons from [Font
Awesome](http://fortawesome.github.io/Font-Awesome/).

Most social widgets that blogs uses are loud and obtrusive. Their colors
and placement takes away reader's attention from the article's content.
To mitigate this problem, Elegant uses muted color for these icons.

<img class="align-left" style="width: 134.0px; height: 72.0px;" src="|filename|/images/social-profiles-sidebar-facebook.png" alt="Hover over Facebook icon in the sidebar" />

<img class="align-left" style="width: 139.0px; height: 69.0px;" src="|filename|/images/social-profiles-sidebar-twitter.png" alt="Hover over Twitter icon in the sidebar" />

These icons change color when users hover over them.

Configuring this *widget* is pretty easy. You need to define `SOCIAL` in
your `pelicanconf.py`. `SOCIAL` is list of tuple. Each tuple has two
items, title and URL.

    :::python

    SOCIAL = (('Twitter', 'http://twitter.com/talham_'),
        ('Github', 'http://github.com/talha131'))

Title of the tuple, for example `Twitter` is used to decide the icon of
you of the social media profile. Elegant picks the icon from Font
Awesome. For example `Twitter` will use `fa-twitter` icon, `Github` will
use `fa-github` icon, and `Facebook` will use `fa-facebook` icon. Your
can see these and other icons in [Font Awesome
documentation](http://fortawesome.github.io/Font-Awesome/icons/#brand).

How to customize the icon
-------------------------

What if the icon of your social media site is not available in Font
Awesome? What if the icon name does not follow `fa-<name>` convention,
for example `Stack Exchange` is different from `fa-stack-exchange`? What
if you want to use `fa-youtube-play` for `Youtube` profile?

The solution is to add a third element to the tuple- icon name.

    :::python

    SOCIAL = (('Twitter', 'http://twitter.com/talham_', 'twitter-square'),
        ('Youtube', 'http://example.com', 'youtube-play'))

This third element is optional. It should be equal to the Font Awesome
CSS class that you want to use for the social profile, minus the `fa`
part from the CSS class name.

How to customize Social Profile Label
-------------------------------------

By default, Elegant labels social profile section as **Contact**. You
can change this label by defining a new variable `SOCIAL_PROFILE_LABEL`
in your `pelicanconf.py` file.

    :::python

    SOCIAL_PROFILE_LABEL = u'Stay in Touch'

