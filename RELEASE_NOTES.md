Version 1.4 (under development)
===============================

* New: Support for `custom.css`
* New: Stat Counter Analytics support
* New: Link to social profiles
* New: Configure heading of social profile with `SOCIAL_PROFILE_LABEL`
* New: `article.comments_intro` that overrides `COMMENTS_INTRO`. Now you can
  define article specific comments introduction
* New: Support for Latex with the help of `latex` plugin
* New: Support for new metadata `modified`
* New: Add Disqus comments to Page
* New: Performance improvement- 4x faster output. 
* New: Use `neighbor` plugin to show next and previous articles
* New: Comments section message changes when user toggles it

Visual Style
------------

* Email newsletter subscriber form style matches rest of the theme
* Article images have a visible border
* Block quotes have a quote icon instead of a thick line on left
* Article's paragraph font size is bigger, for better readability
* Remove unnecessary padding in sidebar's tag list
* Change default place holder text of Email form text field
* Archives page and recent posts on home page have better presentation
* Line number in code block is hidden on tablets and phones to save space for content
* Fix: Nested lists have different font sizes
* Fix: CSS style rules for literal block in reST is missing
* Fix: Long lines in code block will wrap to next line
* Fix: Code block will not play nice with line numbers
* Fix: Subscribe button changes its size on smaller screens
* Fix: Articles under tag heading on tags page are not sorted 
* Fix: URL scheme for blogs which are not published to the root folder

Optimizations
-------------

Following improvements reduce the number of HTTP requests

* Four CSS style sheets have been merged into to one
* Elegant uses minified CSS style sheet
* Favicon is disabled by default. Set `USE_FAVICON` to true to enable it

Behaviour
---------

* Search results link open in the same window, which is consistent with search
  results from internet search engines

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
