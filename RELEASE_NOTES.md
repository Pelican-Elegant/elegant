Version 1.2 (under development)
===============================

* Add CSS style for permanent links. It is visible only user hovers over the heading.

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
