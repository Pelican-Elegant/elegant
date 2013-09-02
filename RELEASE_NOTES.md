Version 1.1 (under testing, stable)
===================================

* Add template for pages. Pages do not have tags, category and Disqus comments
* Keep style of a hyperlink in `modified` meta data consisted with the theme
* Add `keywords` meta tag that uses keywords, tags and category attribute of articles and pages
* Bug fix: Validate search form for empty strings
* Bug fix: Path of search.html in search form action should always be absolute
* Bug fix: Copyright meta tag should be set to the author, instead of the license
* Bug fix: Close meta tags
* Bug fix: ID of search form in 404 page should be different from the ID of search form in main navigation
* Bug fix: If `RECENT_ARTICLES_COUNT` is undefined, set it to 10. So that Pelican does not throw critical error

Version 1.0
===========

* Initial release
