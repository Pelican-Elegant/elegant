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

# Customize Style

To customize Elegant's visual style, use
[`custom.css`](https://github.com/talha131/pelican-elegant/blob/master/static/css/custom.css).
You can override Elegant's visual style like font, color, spacing etc using
this sheet. This empty style sheet is present at following path in your Elegant
folder,

    :::bash
    static/css/custom.css

Find the code of the element you want to customize in
[`elegant.css`](https://github.com/talha131/pelican-elegant/blob/master/static/css/elegant.css).
Copy the element's selector and styles, and paste it in `custom.css`. Edit this
CSS code and customize it to your liking.

Your customizations will override whatever rules are defined in `elegant.css`.

Let's take a look how you can change the style of hyperlinks in an article.
Following is the relevant code,

    :::css
    article p:not(#list-of-translations):not(#post-share-links) a,
    article ol a,
    article div.article-content ul:not(.articles-timeline):not(.related-posts-list) a {

        border-bottom: thin dashed #A9A9A9;
        color: #000;
    }
    
Copy and paste it in `custom.css`. Change color to red for example,

    :::css
    article p:not(#list-of-translations):not(#post-share-links) a,
    article ol a,
    article div.article-content ul:not(.articles-timeline):not(.related-posts-list) a {

        border-bottom: thin dashed #A9A9A9;
        color: red;
    }
    
Test your website using Pelican. All links should be colored red.

Read [this post](avoid-unnecessary-http-requests) to make sure your site's page
speed does not decrease due to additional HTTP request.

# Change Syntax Highlight Theme

Elegant uses [Solarized theme](http://ethanschoonover.com/solarized) for syntax
highlighting. To replace it, copy contents of your preferred theme's CSS style
sheet into `custom.css`.

Alternatively, you can replace contents of `pygments.css` with your theme's
style sheet.

If you feel like experimenting with different themes then [this
repository](https://github.com/uraimo/pygments-vimstyles) has Pygments CSS of
Vim themes. [This one](https://github.com/richleland/pygments-css) has Pygments
CSS of built-in styles. Do not forget to change `.codehilite` CSS class
identifier to `.highlight`. Code blocks in Pelican generated HTML use
`.highlight` class.

# Change Labels

It is quite possible you will feel the need to tweak labels of different
sections or widgets. For example, change label of [social
widget](/how-to-display-your-social-media-profiles) from "Contact" to "Stay in
Touch".

Don't worry! We got you covered!

Elegant has all the customizable variables in one place. [`_defaults.html`
file](https://github.com/talha131/pelican-elegant/blob/master/templates/_includes/_defaults.html).

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

