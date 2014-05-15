Version 2.0 (under development)
===============================

* Link to your social profiles
* Upgraded to Twitter Bootstrap 2.3.2
* Upgraded to Tipue Search 3.1
* Support for `custom.css`
* [Stat Counter Analytics ](http://statcounter.com/) support
* Google Universal Analytics support
* Support for custom icons for social profiles
* Support for Pelican (>3.3) new metadata `modified`
* Support for Social Media Tags
* Support for Google Authorship
* Translations support
* `article.comments_intro` that overrides `COMMENTS_INTRO`. Now you can define
  article specific comments introduction
* Add Disqus comments to Pages
* All customizable variables consolidated in a single `_defaults.html`, making
  it easier for you to customize or even *localize* the theme

Performance
-----------

* Performance improvement- 4x faster output
* Reduce number of HTTP requests using `assets` plugin
* Shortcut icons, like favicon, are disabled by default. Set
  `USE_SHORTCUT_ICONS` to true to enable it

Visual Style
------------

* Email newsletter subscriber form style matches rest of the theme
* Article images have a visible border
* Block quotes have a quote icon instead of a thick line on left
* Article's paragraph font size is bigger, for better readability
* Remove unnecessary padding in sidebar's tag list
* Archives page and recent posts on home page have better presentation
* Time stamps in categories and tags pages are justified
* Line number in code block is hidden on tablets and phones to save space for
  content
* More sizes of image for Apple Touch icons
* Fixed: Nested lists have different font sizes
* Fixed: CSS style rules for literal block in reST is missing
* Fixed: Long lines in code block will wrap to next line
* Fixed: Code block will not play nice with line numbers
* Fixed: Subscribe button changes its size on smaller screens
* Fixed: Articles under tag heading on tags page are not sorted
* Fixed: URL scheme for blogs which are not published to the root folder
* Fixed: Footer is always under the fold even on smaller length web pages
* Fixed: Site Name and top navigation menu move to left on wide displays
* Fixed: Page link is not active in the navbar if `SAVE_PAGE_AS` is not set to
  default

Plugins
-------

* Use `neighbor` plugin to show next and previous articles
* Use `assets` plugin to minify CSS and JS files
* Support for `share_post` plugin
* Support for `related_posts` plugin
* Support for `multi_part` plugin

Behaviour
---------

* Search results link open in the same window, which is consistent with
  internet search engines
* Comments section message changes when user toggles it
* Fixed: Clicking Search button in 404.html does not trigger search

Version 1.3
===========

* Next and previous article navigation is placed below comments section so that article's content and comments appear together
* Article title and site name in `<title>` tag is separated by ` · ` which is cleaner and more subtle than ` -  `
* Subtitle of articles and pages is added in `<title>` tag along with main title
* Description meta tag on Home Page uses `SITE_DESCRIPTION`
* Bug fix: Expand comments section if URL points to a comment
* Bug fix: CSS style of links in an unordered list inside article content is different from article links

Version 1.2
===========

* RSS and Atom feed links
* CSS style for permanent links added. It is visible only user hovers over the heading
* Block quote is indented towards left
* Bug fix: Hyperlink dashed underline is not visible on Chrome
* Bug fix: Text in list goes beyond list marker when text is long and overflows to next line
* Bug fix: Disqus comment count is always 0

Version 1.1
===========

* Add template for pages. Pages do not have tags, category and Disqus comments
* Keep style of a hyperlink in `modified` meta data consisted with the theme
* Add `keywords` meta tag that uses keywords, tags and category attribute of articles and pages
* Validate search form for empty strings
* If `RECENT_ARTICLES_COUNT` is undefined, set it to 10. So that Pelican does not throw critical error
* Bug fix: Path of search.html in search form action should always be absolute
* Bug fix: Copyright meta tag should be set to the author, instead of the license
* Bug fix: Close meta tags
* Bug fix: ID of search form in 404 page should be different from the ID of search form in main navigation
* Bug fix: Links in ordered list in an article do not conform to the link style in rest of the article

Version 1.0
===========

* Initial release
