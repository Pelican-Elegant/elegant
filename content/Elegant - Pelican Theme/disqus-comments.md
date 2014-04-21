Title: How to use Disqus Comments "Elegantly"
Tags: pelican-theme 
Category: Elegant - Pelican Theme
Date: 2014-04-21 16:39
Slug: how-to-use-disqus-comments-elegantly
Disqus_identifier: 9jgwmy8-how-to-use-disqus-comments-elegantly
Subtitle: 
Summary: Elegant offers Disqus comments out of the box with few unique features
Keywords: 

Pelican uses Disqus for comments. You have to set `DISQUS_SITENAME` to Disqus
site name identifier in configuration to enable comments.

But that's not all. Elegant raises the notch up with following unique features.

## Invite Visitors to Comment

Instead of just throwing in comments form at the end of every article, Elegant
offers you a way to write introductory text that would appear right before comments.

![Introductory text to the comments](|filename|/images/elegant-theme_comments-introduction.png)

Set your message to `comments_intro` in the article metadata. You may also
define `COMMENTS_INTRO` in Pelican configuration.  

Write whatever you think is appropriate to invite the visitor to comment. Be
creative! You can even put a link to your twitter account or newsletter there.

Elegant first looks for `comments_intro` in article metadata, then for
`COMMENTS_INTRO` in configuration. If it finds neither then no message is
displayed.

## Disqus Thread ID

Most Pelican themes pass article URL to Disqus as the [Disqus
identifier](http://help.disqus.com/customer/portal/articles/472098-javascript-configuration-variables#disqus_identifier).

This puts you at a disadvantage. If you are forced to change URL of an article
you will lose Disqus discussion for that article because Disqus identifier for
the article will change too.

Elegant offers you `disqus_identifier` property that you can set in your
article metadata. Set it to any unique string you want. It won't be effected by
the article URL.

If you choose not to use `disqus_identifier`, Elegant passes article URL to
Disqus.

