Title: How do I use StatCounter and Google Analytics
Tags: web-analytics
Category: Elegant - Pelican Theme
Date: 2013-11-11 23:05
Slug: how-do-i-use-statcounter-and-google-analytics
Disqus_identifier: 4kv80xq-how-do-i-use-statcounter-and-google-analytics
Subtitle: 
Summary: Elegant Pelican theme supports StatCounter and Google Analytics out of
    the box. This articles describes how to set them up.
Keywords: 

Elegant has support for popular web tracking services,
[StatCounter](http://statcounter.com/) and [Google
Analytics](http://www.google.com/analytics/).

You need to put web property ID, assigned to you by the these services, in your
configuration to use tracking code.

StatCounter
-----------

You need two codes from StatCounter, project ID and security code.

Create a project in StatCounter. Click on Config, Reinstall Code and then
Default Guide. It will show you a standard code that you are
[supposed](http://statcounter.com/support/knowledge-base/14/) to paste in your
website.

    :::javascript
    <!-- Start of StatCounter Code for Default Guide -->
    <script type="text/javascript">
    var sc_project=5555555; 
    var sc_invisible=1; 
    var sc_security="XXXXXXXX"; 
    ...
    <!-- End of StatCounter Code for Default Guide -->

You have to assign `sc_project` value to `STAT_COUNTER_PROJECT` and `sc_security` to `STAT_COUNTER_SECURITY`.

    :::python
    STAT_COUNTER_PROJECT = 5555555
    STAT_COUNTER_SECURITY = u'XXXXXXXX'

That's it. Elegant will take care of the rest.

Google Analytics
----------------

[Get your property
ID](https://support.google.com/analytics/answer/1032385?hl=en) from your Google
Analytics account. It has this format `UA-XXXXX-X`.

Set `GOOGLE_ANALYTICS` variable to it in your configuration.

    :::python
    GOOGLE_ANALYTICS = u'UA-00000000-1'

