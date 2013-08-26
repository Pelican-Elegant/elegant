Title: Elegant
Subtitle: A theme for Pelican
Date: 2013-08-27 23:20
Category: Projects
Tags: jinja2, bootstrap, front-end
Summary: Detailed documentation of Elegant, which is a theme for Pelican, developed using Jinja2 and Bootstrap
Slug: elegant-a-clean-theme-for-pelican-with-search-feature
disqus_identifier: 2189d14-elegant-a-theme-for-pelican


[TOC]


Elegant is a responsive theme for [Pelican](http://getpelican.com/) powered by [Bootstrap](http://twitter.github.com/bootstrap/index.html), in [Jinja2](http://jinja.pocoo.org/). It is a distraction free and clean design. 

## Search

Static sites usually do not offer search. Elegant uses [Tipue Search](http://www.tipue.com/search/)- an open source jQuery plugin, to offer search feature for your static site.

You need to host your site on a server to use the search feature. Currently, there are two search modes that Elegant support.

1. **Live Mode Search** Tipue Search will fetch your site using Sitemap, index it and store it in the visitor's cache. This requires you to have [Sitemap plugin](https://github.com/getpelican/pelican-plugins).
2. **JSON Mode** Your site pages will be stored in JSON at your server. Tipue Search will use AJAX to access it and render search result. This requires you to have [Content in JSON plugin](https://github.com/getpelican/pelican-plugins).

Search box is part of main navigation menu so that visitor can search from anywhere in the site.

![Search box](|filename|/images/elegant-theme_search-box.png)

Here is how the search result page looks like

![Search result for App Store](|filename|/images/elegant-theme_search-result.png)

## Show all categories with less clutter

Pelican by default creates a page for each category. Themes list all the articles filed in that category at its page. Elegant takes a different approach. It lists all the categories and the article on the same page. To reduce clutter and utilise space efficiently, each category and its list of articles in enclosed in [collapsible accordions](http://getbootstrap.com/2.3.2/javascript.html#collapse).

Here is how categories appear collapsed

![Categories accordions collapsed](|filename|/images/elegant-theme_category-accordions-collapsed.png)

And this is how they appear uncollapsed

![Categories accordions uncollapsed](|filename|/images/elegant-theme_category-accordions-uncollapsed.png)

Did you notice that categories are listed in ascending alphabetical order and articles are sorted by their date in descending order?

## Live Filter for Tags

Just like the categories, Elegant follows the same approach for tags. Instead of creating separate pages for each tag, Elegant shows all the tags on a single page. Tags can be in hundreds. To help visitor find the tags he is interested in, Elegant offers live filter. 

Go to tags page and type your required tag in "Find a tag" search box. Elegant will automatically filter the list.

For example, this is how my tags page looks like

![Tags view unfiltered](|filename|/images/elegant-theme_tags-live-filter-default.png)

As soon as I type "os", all other tags are filtered out

![Tags view filtered for "os"](|filename|/images/elegant-theme_tags-live-filter-filtered.png)

## Show comments section only when user clicks on it

When reading an article on the web, readers use scroll bar to track their progress. Very often comments section takes up more space than the actual article. When comments section takes up more space, it throws the scroll bar proportion off. In such cases, reader cannot judge his progress correctly. Hacker News hosted [a discussion](https://news.ycombinator.com/item?id=6246777) on this topic.

> tons of online articles list comments on the same page, so the scroll bar is almost a negative incentive to keep reading.  
> "I've read this much of the article and I'm only 1/20th of the way down?" [user stops reading, unaware that there's 450 comments and the article is actually pretty short]

Elegant keeps the comments section hidden by default. Reader can hide and unhide the section by clicking on the comments section.

This is how comments section appear

![Collapsed comments section](|filename|/images/elegant-theme_comments-section-collapsed.png)

When user clicks on it

![Uncollapsed comments section](|filename|/images/elegant-theme_comments-section-uncollapsed.png)

## Show count of articles with every tag and category

Visitors, who come to your site from a search engine result, usually want to look for related articles on your site. Categories and tags are one such way to show visitor related articles. Elegant display the count of articles that you have written in a category or tag in a non-intrusive manner. 

Every category and tag has the count of articles in superscript. So if you have written three articles in the C++ category or tag, it will have 3 in the superscript.

Check out the screenshots,

![Count of articles in a category is displayed in superscript](|filename|/images/elegant-theme_category-superscript-count.png)


![Count of articles that have been tagged is displayed in superscript](|filename|/images/elegant-theme_tag-superscript-count.png)

## Home Page Features

This is the page that visitors see when they open your website. Elegant tries to show visitors more than just a recent articles list. Check this out

![Home Page Sample](|filename|/images/elegant-theme_home-page-features.png)

You can see two sections here,

1. About me
1. My Projects

There is a third section below these two sections, "Recent articles"

![Recent Articles Section](|filename|/images/elegant-theme_recent-posts.png)

### About me

You can write up your own About me section using `LANDING_PAGE_ABOUT` variable. It is a dictionary that has two keys `title` and `details`. Value of `title` is displayed in the header of the home page, like in the above example it is "I design and build software products for iOS and OSX". `details` is the text that appears under "About me" heading.

### Projects

Projects list is read from `PROJECTS` variable. It is an array of dictionaries. Each dictionary has three keys, `name` which will have name of your project, `url` which will have URL of the project, and `description` which will have the description of the project. You can define as many projects as you. Here is a sample,

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

## Invite users to comment

Some sites just throw the comments section at the end of every article. Elegant offers you to define the introductory text that should appear before comments. Assign your message to `COMMENTS_INTRO` variable in your configuration file.

Write whatever you think is appropriate to invite the visitor to comment. Be creative! You can even put a link to your twitter account or newsletter there. Here is what I have chosen to say to my visitors.

![Introductory text to the comments](|filename|/images/elegant-theme_comments-introduction.png)

## Page Title

Elegant follows following format for the `<title>` tag

```
Article title - Site Name
```

![Article title is always visible in the tab](|filename|/images/elegant-theme_page-title.png)

Some sites put site title first and article title later in the `<title>` tag. There is a problem with this approach.  When you open too many tabs, browser delimits tab's title from the end. In such cases, only the first few words or even letters of the `<title>` are left visible. 

If visitor has opened several tabs from your website, all tabs will have "Site Name..." title. User will need to click on each tab to identify his required tab from the content. But with Elegant's approach article title will always be visible, and user will have less difficultly in identifying the tab he is after. 

Putting site title before the article title increases your site name visibility. Elegant achieves this by putting site name in the top navigation bar of every page, where it always stays above the fold. 

## Show next and previous article with every article

One way to keep the visitor engaged is to show links to articles published before and after the article user is currently reading. Elegant shows newer article on the right hand side and older article on the left hand side at the bottom of every article. Most of the content on web is written in left to right languages. In these languages pages are placed in left to right order. It seemed natural to use the same order in Elegant theme. Elegant does not require on a plugin to show this list.

![Show next and previous articles](|filename|/images/elegant-theme_previous-next-article.png)

## Code style

Elegant uses [Solarized](http://ethanschoonover.com/solarized) theme for syntax highlighting. Line numbers have a distinct background color, as not to mix code with it. Here is an example

    #!c
    int sample_function (void) {
        printf ("This is a sample function");
        return 0
    }


## Mailchimp

Mailchimp has become the preferred newsletter service. Elegant shows a form to subscribe to your newsletter, above the fold, in the right section of every article. Increased visibility is said to increase number of subscribers.

![Mailchimp subscriber form](|filename|/images/elegant-theme_subscribe-form.png)

You need to put your Mailchimp form action URL in `MAILCHIMP_FORM_ACTION` variable in your configuration file. You can also define `EMAIL_SUBSCRIPTION_LABEL`, `EMAIL_FIELD_PLACEHOLDER` and `SUBSCRIBE_BUTTON_TITLE` to customize user experience.

## Disqus Thread ID

Most pelican themes pass article URL to Disqus as the [Disqus identifier](http://help.disqus.com/customer/portal/articles/472098-javascript-configuration-variables#disqus_identifier). This puts you at a disadvantage. If you are forced to change URL of an article you will lose Disqus discussion for that article because Disqus identifier for the articles will change too.

Elegant offers you `disqus_identifier` property that you can set in your article meta data. Set it to any unique string you want. It won't be effected by the article URL.

If you choose not to use `disqus_identifier`, Elegant defaults to article URL and passes it on to Disqus.

## License

You can put your license string in `SITE_LICENSE`. It will appear in the footer of every page of your site. Here is how license of my site looks like,

![onCrashReboot site license](|filename|/images/elegant-theme-license.png)

## Table of Content

The idea behind Elegant design to make reading as less intrusive as possible. Table of contents is important but it is not part of the article content. Elegant pushes out table of content to the left of the article's main content. It's font size is relatively smaller. Reader main focus stays the article but table of content stays visible to use for navigation.

To utilise this feature, you need to use [extract_toc](https://github.com/getpelican/pelican-plugins) pelican plugin. Elegant also encloses the table of content in `<nav>` tag for semantics.

## Subtitle of article

Pelican lets you define title of your article in the meta data. Elegant adds subtitle to it. Just define `subtitle` in your article's meta data and it will appear along with your title. Here is an example,

![Article subtitle example](|filename|/images/elegant-theme_article-subtitle.png)

## Site Subtitle

You can also define `SITESUBTITLE`, it appears in the footer, before site license.

![Site subtitle](|filename|/images/elegant-theme_site-subtitle.png)


## Custom 404 Page

Elegant has a Error 404 page for your readers.

![Error 404 page](|filename|/images/elegant-theme_error-404-page.png)

## Favicon and Speed Dial icon

Every decent site has favicon, Apple launcher icons and Opera speed dial icon. I recommend using [Iconifier.net](http://iconifier.net/) to generate set of images. Place all the images in `content/theme/images` folder. The define `STATIC_PATHS` variable in your configuration

    :::python
    STATIC_PATHS = ['theme/images', 'images']   

Your images should have these naming schemes

1. `apple-touch-icon-114x114.png` 
1. `apple-touch-icon-144x144.png`
1. `apple-touch-icon-57x57.png`
1. `apple-touch-icon-72x72.png`
1. `apple-touch-icon.png`
1. `favicon.ico`

## Modified date

You will need to update your articles time and again. You can show date article was last updated by defining `modified` variable in your article meta data. You should put the date you last modified the article. Please note that value of `modified` is treated as string. This is how it is displayed in the side bar,

![Date Modified](|filename|/images/elegant-theme_last-modified.png)

## SEO

Your `SITE_DESCRIPTION` and article summary is used to define description meta tag `<meta name="description">`.

Your site license is also placed in copyright meta tag `<meta name="copyright"`. 

## Web safe fonts

I have tried to use proper fall back font for every style. For examples headings primarily used Baskerville font. But if the reader does not have Baskerville, he will have Garamond. If that too fails then at least Georgia will be present on his system.

# Sample Configuration

Here are the variables that you should set in your configuration to get the most out of Elegant

    :::python
    PLUGINS = ['sitemap', 'extract_toc', 'content_in_json']
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

# License

The license requires that you give credit to me, Talha Mansoor, as the author of the Elegant theme on every site that uses this theme. I have placed the attribution in the footer of every page. Do not remove it. If you need to remove or change the style of the attribution, please get in [touch with me](http://oncrashreboot.com/#about-me) first. 

With this attribution clause, Elegant theme is licensed under The MIT License.

# Contribute

Front end design is not my strong suite. I must have made some blunders in this design unknowingly. Please don't let me go away with buggy code.   

File bugs at [Github issues](https://github.com/talha131/pelican-elegant/issues).  
Share your ideas about the design in the comments below.  
And most of all contribute improvements to [this project](https://github.com/talha131/pelican-elegant/).

These are the problem areas that bug me and I need your help to fix them,

1. Internet Explorer support
1. Web safe fonts. I developed this theme on a MacBook Retina. Although I have tried to make sure it looks great on all platforms but it still needs polish

