Title: Elegant
Subtitle: A theme for Pelican
Date: 2013-08-27 23:20
Category: Projects
Tags: jinja2, bootstrap, front-end
Summary: Detailed documentation of Elegant, which is a theme for Pelican, developed using Jinja2 and Bootstrap
Slug: elegant-a-clean-theme-for-pelican-with-search-feature
disqus_identifier: 2189d14-elegant-a-theme-for-pelican
modified: <a href="https://github.com/talha131/onCrashReboot/commits/master/content/Projects/elegant-theme.md" title="Revision History">Aug 29, 2013</a>


[TOC]


Elegant is a responsive theme for [Pelican](http://getpelican.com/) powered by [Bootstrap](http://twitter.github.com/bootstrap/index.html), and developed in [Jinja2](http://jinja.pocoo.org/). It is a minimal, and stylish theme that looks amazing across all screen resolutions and devices. 

Elegant gives meaning to the expression "sand the under side of the drawer." Every feature and style of Elegant is the result of a long thought process. 

<div style="text-align:center;">
<button class="btn btn-large btn-primary" type="button" onclick="window.open('https://github.com/talha131/pelican-elegant', '_blank');">Get Elegant</button>
</div>

What makes Elegant so special? 

## Search

Static sites usually do not offer search. Elegant uses [Tipue Search](http://www.tipue.com/search/)- an open source jQuery plugin, to offer search for your static site.

There are two search modes.

1. **JSON Mode** Your site pages will be stored in JSON at your server. Tipue Search will use AJAX to access it and render search result. You need [Tipue Search plugin](https://github.com/getpelican/pelican-plugins) to use this mode.
1. **Live Mode Search** Tipue Search will fetch your site using Sitemap, index it and store it in the visitor's cache. This mode requires [Sitemap plugin](https://github.com/getpelican/pelican-plugins).

Use JSON mode if you value speed, or have a large site, or don't want to overwhelm your host server for every search query.

Here is how the search result looks like

![Search result for App Store](|filename|/images/elegant-theme_search-result.png)

Search box is part of main navigation menu so that visitor can search from any page.

![Search box](|filename|/images/elegant-theme_search-box.png)

## Live Filter for Tags

Elegant is a minimal theme. Instead of creating separate pages for each tag, Elegant shows all the tags on a single page. To help visitor find the tags he is interested in, Elegant offers live filter. 

Go to tags page and type your required tag in "Find a tag" search box. Elegant will automatically filter the list.

For example, this is how my tags page looks like

![Tags view unfiltered](|filename|/images/elegant-theme_tags-live-filter-default.png)

As soon as I type "os", all other tags are filtered out

![Tags view filtered for "os"](|filename|/images/elegant-theme_tags-live-filter-filtered.png)

With live filter, your reader will have no difficulty in picking up his desired tag from the list, even if your site has hundreds of tags.

## All Categories but with zero clutter

Pelican by default creates a separate page for each category. Themes list all the articles filed in that category at its page. Elegant takes a different approach. 

It lists all the categories and their articles on the same page. To reduce clutter and utilise space efficiently, each category and its list of articles in enclosed in [collapsible accordions](http://getbootstrap.com/2.3.2/javascript.html#collapse).

Here is how categories appear collapsed

![Categories accordions collapsed](|filename|/images/elegant-theme_category-accordions-collapsed.png)

And this is how they appear uncollapsed

![Categories accordions uncollapsed](|filename|/images/elegant-theme_category-accordions-uncollapsed.png)

Did you notice that categories are listed in ascending alphabetical order and articles are sorted by their date in descending order?

## Home Page Features

This is the page that visitors see when they open your website. Your chance to make a good and lasting first impression. Most sites just display a list of recent posts. Elegant goes the extra mile. Check this out

![Home Page Sample](|filename|/images/elegant-theme_home-page-features.png)

You can see two sections here,

1. About me
1. My Projects

There is a third section below these two sections, "Recent articles"

![Recent Articles Section](|filename|/images/elegant-theme_recent-posts.png)

### About me

You can write up your own About me section using `LANDING_PAGE_ABOUT` variable in your configuration. It is a dictionary that has two keys `title` and `details`. Value of `title` is displayed in the header of the home page, like in the above example it is "I design and build software products for iOS and OSX". `details` is the text that appears under "About me" heading.

### Projects

Projects list is read from `PROJECTS`. It is an array of dictionaries. Each dictionary has three keys, `name` which will have name of your project, `url` which will have URL of the project, and `description` which will have the description of the project. You can define as many projects as you want. Here is an example,

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

Recent articles show last `RECENT_ARTICLES_COUNT`. It also has a link to "all posts".

## Mailchimp

Mailchimp has become the preferred newsletter service. Elegant shows a form to subscribe to your newsletter, above the fold, in the right section of every article. Increased visibility is said to increase number of subscribers.

![Mailchimp subscriber form](|filename|/images/elegant-theme_subscribe-form.png)

You need to put your Mailchimp form action URL in `MAILCHIMP_FORM_ACTION` in your configuration file. You can also define `EMAIL_SUBSCRIPTION_LABEL`, `EMAIL_FIELD_PLACEHOLDER` and `SUBSCRIBE_BUTTON_TITLE` to customize user experience.

## Collapsible Comments

Readers use scroll bar to track their progress when reading inside their browsers. Very often comments take up more space than the actual article. When comments take up more space, it throws the scroll bar proportion off and reader cannot judge his progress correctly. Hacker News hosted [a discussion](https://news.ycombinator.com/item?id=6246777) on this topic.

> tons of online articles list comments on the same page, so the scroll bar is almost a negative incentive to keep reading.  
> "I've read this much of the article and I'm only 1/20th of the way down?" [user stops reading, unaware that there's 450 comments and the article is actually pretty short]

Elegant keeps the comments section hidden by default. Reader can hide and unhide the section by clicking on the comments section.

This is how comments section appear

![Collapsed comments section](|filename|/images/elegant-theme_comments-section-collapsed.png)

It expands when reader clicks on it

![Uncollapsed comments section](|filename|/images/elegant-theme_comments-section-uncollapsed.png)

## Invite Visitors to Comment

Instead of just throwing in comments' form at the end of every article, Elegant offers you a way to write introductory text that would appear before comments. Assign your message to `COMMENTS_INTRO` in your configuration file.

Write whatever you think is appropriate to invite the visitor to comment. Be creative! You can even put a link to your twitter account or newsletter there. Here is what I have chosen to say to my visitors.

![Introductory text to the comments](|filename|/images/elegant-theme_comments-introduction.png)

## Articles Count with every Tag and Category

Readers of an article on your site usually look for other articles on the same topic. Categories and tags are a way of showing them related articles. Elegant displays the count of articles that you have written in a category or tag in a non-intrusive manner. 

Every category and tag has the count of articles in superscript. So if you have written three articles in the C++ category or tag, it will have 3 in the superscript. This way visitor will know you have written other articles too on the same topic.

Check out the screenshots,

![Count of articles in a category is displayed in superscript](|filename|/images/elegant-theme_category-superscript-count.png)


![Count of articles that have been tagged is displayed in superscript](|filename|/images/elegant-theme_tag-superscript-count.png)

## Custom 404 Page

Elegant has a custom Error 404 page for your readers.

![Error 404 page](|filename|/images/elegant-theme_error-404-page.png)

## Page Title

Elegant follows following format for the `<title>` tag

```
Article title - Site Name
```

![Article title is always visible in the tab](|filename|/images/elegant-theme_page-title.png)

Some sites put site title first and article title later in the `<title>` tag. There is a problem with this approach.  When you open too many tabs, browser delimits tab's title from the end. In such cases, only the first few words or even letters of the `<title>` are left visible. 

If visitor has opened several tabs from your website, all tabs will have "Site Name..." title. User will need to click on each tab to identify his required tab from the content. But with Elegant's approach article title will always be visible, and reader will have less difficultly in identifying the tab he is after. 

Putting site title before the article title increases your site name visibility. Elegant achieves this by putting site name in the top navigation bar of every page, where it always stays above the fold. 

## Next and Previous Articles

One way to keep the visitor engaged is to show links to articles published before and after the article visitor is currently reading. Elegant shows newer article on the right hand side and older article on the left hand side at the bottom of every article. 

Most of the content on web is written in left to right languages. In these languages pages are placed from left to right. It seemed natural to use the same order in Elegant. 

![Show next and previous articles](|filename|/images/elegant-theme_previous-next-article.png)

Elegant does not require any plugin to show this list.

## Code Style

Elegant uses [Solarized](http://ethanschoonover.com/solarized) theme for syntax highlighting. Line numbers have a different background color so that they appear distinct from the code. Here is an example

    #!c
    int sample_function (void) {
        printf ("This is a sample function");
        return 0
    }


## Disqus Thread ID

Most pelican themes pass article URL to Disqus as the [Disqus identifier](http://help.disqus.com/customer/portal/articles/472098-javascript-configuration-variables#disqus_identifier). This puts you at a disadvantage. If you are forced to change URL of an article you will lose Disqus discussion for that article because Disqus identifier for the article will change too.

Elegant offers you `disqus_identifier` property that you can set in your article meta data. Set it to any unique string you want. It won't be effected by the article URL.

If you choose not to use `disqus_identifier`, Elegant defaults to article URL and passes it on to Disqus.

## Add License to your Site

You can put your license string in `SITE_LICENSE`. It will appear in the footer of every page of your site. Here is how license of my site looks like,

![onCrashReboot site license](|filename|/images/elegant-theme-license.png)

## Table of Content

The idea behind Elegant's design is to make reading a clean and distraction free experience. Table of contents is important but it is not part of the article content. Therefore, Elegant pushes out table of content to the left of the article's main content. Its font size is relatively smaller. This way, table of content stays visible for navigation but reader's attention to the article stays unaffected.

To utilise this feature, you need to use [extract_toc](https://github.com/getpelican/pelican-plugins) pelican. Elegant encloses the table of content in `<nav>` tag for semantics.

## Article Subtitle

Pelican lets you define title of your article in the meta data. Elegant adds subtitle support. Just define `subtitle` in your article's meta data and it will appear along with your title. Here is an example,

![Article subtitle example](|filename|/images/elegant-theme_article-subtitle.png)

Article subtitle is displayed with the title in every list. To keep it visibly separate from title, subtitle is enclosed in `<small>` tag. When visible cue cannot be used, like in the title attribute of html anchor tag `<a>`, a hyphen is inserted between them.

![Article title and subtitle separated with a hyphen](|filename|/images/elegant-theme_article-subtitle-hyphen.png)

## Site Subtitle

You can also define `SITESUBTITLE`, it appears in the footer, before site license.

![Site subtitle](|filename|/images/elegant-theme_site-subtitle.png)


## Favicon and Speed Dial icon

Every decent site has favicon, Apple launcher icons and Opera speed dial icon. Elegant supports all of them.

Place your images in `content/theme/images` directory, and define `STATIC_PATHS` variable in your configuration

    :::python
    STATIC_PATHS = ['theme/images', 'images']   

Your images should have follow these naming schemes

1. `apple-touch-icon-114x114.png` 
1. `apple-touch-icon-144x144.png`
1. `apple-touch-icon-57x57.png`
1. `apple-touch-icon-72x72.png`
1. `apple-touch-icon.png`
1. `favicon.ico`

I recommend using [Iconifier.net](http://iconifier.net/) to generate the set of images. 

## Modified Date

You will need to update your articles time and again. You can show the date article was last updated by defining `modified` in your article meta data. 

This is how it is displayed in the side bar,

![Modified Date](|filename|/images/elegant-theme_last-modified.png)

Value of `modified` is treated as string, thus you can insert raw HTML in it. For example, `modified` meta data for this article is

    :::html
    modified: <a href="https://github.com/talha131/onCrashReboot/commits/master/content/Projects/elegant-theme.md" title="Revision History">Aug 29, 2013</a>

Clicking on "Aug 29, 2013" will take reader to the Git repository which will show him revision history of the article.

## Efficient use of Meta Tags 

Your `SITE_DESCRIPTION` and article summary is used to define description meta tag `<meta name="description"`.

Your site license is also placed in copyright meta tag `<meta name="copyright"`. 

## Web Safe Fonts

Elegant uses commonly available typefaces in every style rule. It has a list of closely matching fonts in the fallback list. For examples Baskerville is the first choice for headings. But if reader does not have Baskerville installed, Garamond will be used. If that too fails then Georgia will be used.

***************************

# Elegant - Technical Nitty-Gritty

## Configuration Variables

Here are the variables that you should set in your configuration to get the most out of Elegant

    :::python
    PLUGINS = ['sitemap', 'extract_toc', 'tipue_search']
    MD_EXTENSIONS = ['codehilite(css_class=highlight)', 'extra', 'headerid', 'toc']
    DIRECT_TEMPLATES = (('index', 'tags', 'categories','archives', 'search', '404'))
    STATIC_PATHS = ['theme/images', 'images']
    TAG_SAVE_AS = ''
    CATEGORY_SAVE_AS = ''
    AUTHOR_SAVE_AS = ''

These are the optional configuration variables that you can define

    :::python
    RECENT_ARTICLES_COUNT (integer)  
    COMMENTS_INTRO ('string')
    SITE_LICENSE ('string')
    SITE_DESCRIPTION ('string')
    EMAIL_SUBSCRIPTION_LABEL ('string')
    EMAIL_FIELD_PLACEHOLDER ('string')
    SUBSCRIBE_BUTTON_TITLE ('string')
    MAILCHIMP_FORM_ACTION ('string')
    SITESUBTITLE ('string')
    LANDING_PAGE_ABOUT ({})
    PROJECTS ([{},...])

These are the optional article meta data variables that you can use

    :::python
    subtitle
    summary
    disqus_identifier
    modified

Blog [`onCrash=Reboot();`](http://oncrashreboot.com) uses Elegant theme. You can see its configuration files at [Github](https://github.com/talha131/onCrashReboot) for inspiration.

## License

The license requires that you give credit to me, Talha Mansoor, as the author of the Elegant theme on every site that uses this theme. I have placed the attribution in the footer of every page. Do not remove it. If you need to remove or change the style of the attribution, please get in [touch with me](http://oncrashreboot.com/#about-me) first. 

Along with this attribution clause, Elegant theme is licensed under The MIT License.

If you use my theme, I would love to hear from you. [Get in touch](http://oncrashreboot.com/#about-me) and let me know about it. I may link to your site too.

## Contribute

Front end design is not my strong suite. I must have made some blunders in this design unknowingly. Please don't let me go away with buggy code.   

* File bugs at [Github issues](https://github.com/talha131/pelican-elegant/issues).  
* Share your ideas about the design in the comments below.  
* And most of all contribute improvements to [this project](https://github.com/talha131/pelican-elegant/).

There are two problem areas that I can think of,

1. Internet Explorer support
1. Web safe fonts. I developed this theme on a MacBook Retina. Although I have tried to make sure it looks great on all platforms but it still needs polish

Besides these, there must be other bugs that I haven't noticed yet. I need your help to hunt them down and make them behave.

