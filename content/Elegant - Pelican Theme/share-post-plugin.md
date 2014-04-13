Title: How to use Social Sharing Plugin
Tags: pelican-theme 
Category: Elegant - Pelican Theme
Date: 2014-03-24 20:14
Slug: how-to-use-social-sharing-plugin
Disqus_identifier: x4jitcv-how-to-use-social-sharing-plugin
Subtitle: 
Summary: Elegant integrates with Share Post plugin of Pelican out of the box
Keywords: social networks, share posts,

No blog is complete without a social sharing plugin, that invites visitors to
share your post on popular social networks. 

There are plethora of social sharing widgets available online. Unfortunately
most of these widgets are used to track users. [Technology
watchdogs](http://techliberation.com/2011/05/20/privacy-solutions-how-to-block-facebooks-like-button-and-other-social-widgets/)
have been [raising a hue and
cry](http://online.wsj.com/news/articles/SB10001424052748704281504576329441432995616#printMode)
since as [early as
2009](https://www.eff.org/deeplinks/2009/09/online-trackers-and-social-networks).

Developers have come up with [different ways](http://fixtracking.com/) to cope
this issue. Solutions ranging from [browser plugins](https://disconnect.me/) to
totally [reinventing share
widgets](http://panzi.github.io/SocialSharePrivacy/).

Obviously, you cannot expect that all your visitors to use a privacy plugin.
Most browsers on mobile platforms do not let user install any sort of plugin.

Reinventing social widget will require educating users about it. The new style
will be alien to them and may result in a decrease in number of *shares* on
social networks.

Elegant has a far simpler solution. It uses Pelican's [Share
Post](https://github.com/getpelican/pelican-plugins/tree/master/share_post)
plugin. This plugin generates old school URLs that cannot be used for online
tracking at all.

Elegant supports it out of the box. You just have to enable it in your Pelican
configuration,

    :::python
    PLUGINS = ['share_post']

And viola!

![Share Post plugin in Elegant](|filename|/images/elegant-theme-share-post-plugin.png)

Like [rest of the Elegant](how-to-customize-elegant) you can customize this
widget too.

You can define `SHARE_POST_INTRO` in your Pelican configuration to override the
default "Share on:" text.

You can also define it on per article basis by defining `share_post_intro` in
your article metadata.

