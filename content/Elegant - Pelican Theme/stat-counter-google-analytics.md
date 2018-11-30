Title: How to use StatCounter and Google Analytics
Tags: web-analytics, pelican-theme
Category: Elegant - Pelican Theme
Date: 2013-11-11 23:05
Slug: how-to-use-statcounter-and-google-analytics
Disqus_identifier: 4kv80xq-how-to-use-statcounter-and-google-analytics
Subtitle:
Summary: Elegant Pelican theme supports StatCounter and Google Analytics out of
    the box. This articles describes how to set them up.
Keywords:

[TOC]

Elegant has support for popular web tracking services,
[StatCounter](http://statcounter.com/), [Google
Analytics](http://www.google.com/analytics/) and [Heap](https://heapanalytics.com/).

You have to put web property ID assigned to you by the these services, in your
configuration to use the tracking code.

StatCounter
-----------

You need two codes from StatCounter- project ID and security code.

Create a project in StatCounter. Click on Config, Reinstall Code and then
Default Guide.

It will show you a [standard
code](http://statcounter.com/support/knowledge-base/14/)
that a website must have in order to use StatCounter.

    :::javascript
    <!-- Start of StatCounter Code for Default Guide -->
    <script type="text/javascript">
    var sc_project=5555555;
    var sc_invisible=1;
    var sc_security="XXXXXXXX";
    ...
    <!-- End of StatCounter Code for Default Guide -->

Assign `sc_project` value to `STAT_COUNTER_PROJECT` and `sc_security` to `STAT_COUNTER_SECURITY`.

    :::python
    STAT_COUNTER_PROJECT = 5555555
    STAT_COUNTER_SECURITY = u'XXXXXXXX'

Google Analytics
----------------

[Get your property
ID](https://support.google.com/analytics/answer/1032385?hl=en) from your Google
Analytics account. It has this format `UA-XXXXX-X`.

Set `GOOGLE_ANALYTICS` variable to it in your configuration.

    :::python
    GOOGLE_ANALYTICS = u'UA-00000000-1'

That's it. Elegant will take care of the rest.

Heap
----

From your [Heap console](https://heapanalytics.com/app/account), navigate to
Settings->Projects. You need to copy the Project ID you want to log to.
Set `HEAP_ANALYTICS` in your configuration with this value.

    :::python
    HEAP_ANALYTICS = 1234567890

Elegant will take care of the rest once that value is added.
