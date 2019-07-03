Title: How to Customize Elegant
Tags: pelican-theme, config
Category: Elegant - Pelican Theme
Date: 2014-03-24 14:05
Slug: how-to-customize-elegant
Disqus_identifier: ale31i7-how-to-customize-elegant
Subtitle:
Summary: You can customize every aspect of Elegant without touching the source code
Keywords:

[TOC]

You can change Elegant's look, color palette, font, size, and even labels used
for widgets, sections and plugins.

Elegant is best maintained when you treat it as a separate resource in your
project. Do not edit template files, JavaScript code and style sheets. This
practice will make upgrading Elegant fuss free process.

Instead use following recommended ways.

# Change Labels

It is quite possible you will feel the need to tweak labels of different
sections or widgets. For example, change label of [social
widget](/how-to-display-your-social-media-profiles) from "Contact" to "Stay in
Touch".

Don't worry! We got you covered!

Elegant has all the customizable variables in one place. [`_defaults.html`
file](https://github.com/Pelican-Elegant/elegant/blob/master/templates/_includes/_defaults.html).

    :::bash
    templates/_includes/_defaults.html

Let's see how can we change social widget label.

    #!jinja
    {# Label for the list of social profiles #}
    {% if not SOCIAL_PROFILE_LABEL %}
    {% set SOCIAL_PROFILE_LABEL = 'Contact' %}
    {% else %}
    {% set SOCIAL_PROFILE_LABEL = SOCIAL_PROFILE_LABEL %}
    {% endif %}

Line 1, text enclosed in `{# #}` is a comment, which says this section is about
"Label for the list of social profiles".

The text in all capital case `SOCIAL_PROFILE_LABEL` is the actual variable.

Line 3 says `SOCIAL_PROFILE_LABEL` is set to `Contact`.

To change this value, assign it a different value in your Pelican
configuration, `pelicanconf.py`.

    :::python
    SOCIAL_PROFILE_LABEL = 'Stay in Touch'

That's it. The title of social widget will change. There are several others
labels that you can customize easily without touching Elegant's source code.
