Title: Configuration Variables and Metadata List
Tags: pelican-theme, config
Category: Elegant - Pelican Theme
Date: 2014-04-23 18:25
Slug: configuration-variables-and-metadata-list
Disqus_identifier: dexlwa8-configuration-variables-and-metadata-list
Subtitle: 
Summary: List of all the configuration variables and metadata that you can use with Elegant
Keywords: 

[TOC]

## Pelican Configuration

These are the settings that will help you get the most out of Elegant

    #!python
    TAG_SAVE_AS = ''
    AUTHOR_SAVE_AS = ''
    CATEGORY_SAVE_AS = ''
    STATIC_PATHS = ['theme/images', 'images']
    PLUGINS = ['sitemap', 'extract_toc', 'tipue_search',
               'neighbors', 'assets', 'share_post']
    MD_EXTENSIONS = ['codehilite(css_class=highlight)', 'extra',
                     'headerid', 'toc(permalink=true)']
    DIRECT_TEMPLATES = (('index', 'tags', 'categories','archives', 'search', '404'))

## Configuration Variables

These are the optional configuration variables that you can define

1. `PROJECTS` used for [Projects
   feature](elegant-best-pelican-theme-features#projects)
   on the landing page
1. `PROJECTS_TITLE` used for changing title of `PROJECTS` list
1. `USE_SHORTCUT_ICONS` used for [shortcut icons like favicon, Opera Speed
   Dial](how-to-set-shortcut-icons)
1. `SITE_LICENSE` used to add [site
   license](few-more-features-of-elegant#add-license-to-your-site)
1. `SITE_SUBTITLE` used to add [site subtitle in the
   footer](few-more-features-of-elegant#site-subtitle)
1. `COMMENTS_INTRO` used with
   [comments](how-to-use-disqus-comments-elegantly#invite-visitors-to-comment)
1. `SITE_DESCRIPTION` used for [Search Engine
   Optimization](search-engine-and-social-media-optimization#search-engine-optimization-seo)
1. `LANDING_PAGE_ABOUT` used for [About me
   feature](elegant-best-pelican-theme-features#about-me)
   on the landing page
1. `SOCIAL_PROFILE_LABEL` used with [social media profiles
   widget](how-to-display-your-social-media-profiles)
1. `RECENT_ARTICLES_COUNT` see the post [Recent
   Articles](elegant-best-pelican-theme-features#recent-articles)

These are the variables used for [Mailchimp subscriber
form](elegant-best-pelican-theme-features#mailchimp) in the sidebar,

1. `MAILCHIMP_FORM_ACTION` is mandatory. Set it to your Mailchimp form action
   URL
1. `SUBSCRIBE_BUTTON_TITLE`
1. `EMAIL_FIELD_PLACEHOLDER`
1. `EMAIL_SUBSCRIPTION_LABEL`

These are the variables used with different Pelican plugins,

1. `SERIES_TITLE` used with [`multi_part` plugin](how-to-use-multi-part-plugin)
1. `SHARE_POST_INTRO` used with [`share_post`
   plugin](how-to-use-social-sharing-plugin)
1. `RELATED_POSTS_LABEL` used with [`related_posts`
   plugin](https://github.com/getpelican/pelican-plugins/tree/master/related_posts) 

These are the variables used for [Social Media
Optimization](search-engine-and-social-media-optimization#social-media-optimization-smo),

1. `FEATURED_IMAGE`
1. `TWITTER_USERNAME`

This site uses Elegant theme. You
can view its configuration files at
[Github](https://github.com/Pelican-Elegant/documentation) for inspiration.

## Metadata

Pelican uses [file
metadata](http://docs.getpelican.com/en/latest/getting_started.html#file-metadata)
from your articles and pages text files to get information about your posts,
like tags, authors etc.

On top of *"official"* metadata, Elegant uses some optional metadata that you
can use in your articles and pages.

1. `summary` used for [Search Engine
    Optimization](search-engine-and-social-media-optimization#search-engine-optimization-seo)
1. `subtitle` used to set [article
    subtitle](elegant-best-pelican-theme-features#article-subtitle)
1. `keywords` used for [Search Engine
    Optimization](search-engine-and-social-media-optimization#search-engine-optimization-seo)
1. `modified` used to set [last updated time](how-does-modified-metadata-works)
    of the article
1. `series_title` used with [`multi_part` plugin](how-to-use-multi-part-plugin)
1. `featured_image` used for [Social Media
    Optimization](search-engine-and-social-media-optimization#social-media-optimization-smo)
1. `comments_intro` used with
    [comments](how-to-use-disqus-comments-elegantly#invite-visitors-to-comment)
1. `share_post_intro` used with [`share_post`
    plugin](how-to-use-social-sharing-plugin)
1. `disqus_identifier` used with
    [comments](how-to-use-disqus-comments-elegantly#disqus-thread-id)

