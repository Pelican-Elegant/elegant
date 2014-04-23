Title: Search Engine and Social Media Optimization
Tags: pelican-theme, social-media
Category: Elegant - Pelican Theme
Date: 2014-04-20 16:31
Slug: search-engine-and-social-media-optimization
Disqus_identifier: 7mh4xjn-search-engine-and-social-media-optimization
Summary: 
Keywords: 

[TOC]

Search Engine Optimization(SEO) is a moving target which is often
misunderstood.  Rise of social media has changed the traditional SEO
techniques. Changes in search algorithms has made several SEO tecniques
obsolete.

Elegant does its best to leverage all available search and social media tags to
give your site higher ranking in search results and optimize it for sharing via
social media.

## Social Media Optimization (SMO)

Inspired by the post ["What is the New SEO? Pubcon 2013
Takeaways"](https://medium.com/on-startups/f15264e5d790), I looked into the
tags that social media sites use. They can be broadly divided into two
categories, [Open Graph protocol](http://ogp.me/) and [Twitter
Cards](https://dev.twitter.com/docs/cards).

### Open Graph protocol

Elegant uses following tags,

1. `og:url` is set to article URL
1. `og:type` is set to "article"
1. `og:title` is set to article tile and optional subtitle
1. `og:site_name` is set to `SITENAME` from your Pelican configuration
1. `og:description` is set to article summary
1. `og:article:author` is set to article author
1. `og:article:published_time` is set to article date
1. `og:image` is an optional tag. It is set to value of `featured_image`

`featured_image` should be the complete URL of an image. This image is
displayed with the article link on most social sites.

Elegant looks for it first in the article metadata, here is metadata for an
example reST formated file.

    :::reST
    :featured_image: http://oncrashreboot.com/images/article-1-image.jpg

Then it looks for `FEATURED_IMAGE` in Pelican configuration. If it finds
neither, `og:image` is not used.

If you want to use `og:image` tag then make sure you define `featured_image` in
your article metadata. You should also define `FEATURED_IMAGE` in your
Pelican configuration to be used as a generic image in case an article does not
have `featured_image` defined.

### Twitter Cards

Elegant uses following tags,

1. `twitter:card` is set to "summary"
1. `twitter:title` is set to article title and optional subtitle
1. `twitter:creator` is set to `TWITTER_USERNAME` if defined in Pelican
   configuration 
1. `twitter:description` is set to article summary
1. `twitter:image` is set to `featured_image`. The `featured_image` discussion
   above is also applicable in this case

Please note you need to be
[approved](https://dev.twitter.com/docs/cards/validation/validator) by Twitter
before you can start using Twitter Cards.

## Search Engine Optimization (SEO)

Elegant puts tags and category of your article in keywords tag `<meta
name="keywords"`. 

You can add your own keywords by defining `keywords` in article metadata.

`SITE_DESCRIPTION` and article `summary` is used in description tag `<meta
name="description"`.

Your `AUTHOR` name is used in copyright tag `<meta name="copyright"`. 

## Google+

On the topic of Google+, article ["What is the New SEO? Pubcon 2013
Takeaways"](https://medium.com/on-startups/f15264e5d790#6f78) has this to say,

> Regardless of your opinion of Google the company or Google+ the service,
> using Google+ as a channel for social signaling, content distribution, and
> traffic is a requirement going forward. 

Also, 

> To take advantage of this today you’ve got a few options. As an author you
> create a Google+ profile and link to this profile from every site you publish
> on using the tag rel=”author”. Then, through your “about” page on Google+,
> you can reference the domains you publish to, completing the Google+
> authorship link.

In view of these recommendations, Elegant lets you link to your Google+ profile
using `rel="author"`.

Assign your Google+ profile link to `GOOGLE_PLUS_PROFILE_URL` in Pelican
configuration and you are done.

Google help article ["Author information in search
results"](https://support.google.com/webmasters/answer/1408986?hl=en) mentions
one more way of linking - use a verified email address.

Use whichever way suits you.

