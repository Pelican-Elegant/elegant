# [3.2.0](https://github.com/Pelican-Elegant/elegant/compare/V3.1.0...V3.2.0) (2019-07-30)

### Bug Fixes

- **freelists:** open FreeLists subscription form in a new tab ([f81657c](https://github.com/Pelican-Elegant/elegant/commit/f81657c))
- **freelists:** replace deprecated subscription form with button ([9bfe3c1](https://github.com/Pelican-Elegant/elegant/commit/9bfe3c1)), closes [#412](https://github.com/Pelican-Elegant/elegant/issues/412)
- **freelists:** rm unused include ([27f0831](https://github.com/Pelican-Elegant/elegant/commit/27f0831))

### Features

- **comments:** reduce transition duration from 500 to 200 ([b86e13d](https://github.com/Pelican-Elegant/elegant/commit/b86e13d))
- **favicon:** add 180x180 dimension shortcut icon support ([dd2ed24](https://github.com/Pelican-Elegant/elegant/commit/dd2ed24))
- **filter:** add black list, white list feature for Disqus ([4887aec](https://github.com/Pelican-Elegant/elegant/commit/4887aec))
- **filter:** add black list, white list feature for FreeLists ([2407cc8](https://github.com/Pelican-Elegant/elegant/commit/2407cc8))
- **filter:** add black list, white list feature for Mailchimp ([b96122d](https://github.com/Pelican-Elegant/elegant/commit/b96122d))

# [3.1.0](https://github.com/Pelican-Elegant/elegant/compare/V3.0.0...V3.1.0) (2019-07-14)

### Bug Fixes

- **article:** fix regression introduced in 7ca7331c0 ([2c23961](https://github.com/Pelican-Elegant/elegant/commit/2c23961))
- **authors:** title attribute was not closed in quotes ([de1d05b](https://github.com/Pelican-Elegant/elegant/commit/de1d05b))
- **gist:** embedded Github gist are not laid out correctly ([0416433](https://github.com/Pelican-Elegant/elegant/commit/0416433)), closes [#123](https://github.com/Pelican-Elegant/elegant/issues/123)
- **reST:** indents in line blocks is not preserved ([e1429c5](https://github.com/Pelican-Elegant/elegant/commit/e1429c5)), closes [#144](https://github.com/Pelican-Elegant/elegant/issues/144)

### Features

- **article:** make article subtitle italic ([7ca7331](https://github.com/Pelican-Elegant/elegant/commit/7ca7331)), closes [#284](https://github.com/Pelican-Elegant/elegant/issues/284)
- **authors:** add line above authors section ([35a35b0](https://github.com/Pelican-Elegant/elegant/commit/35a35b0))
- **authors:** add support for avatar ([cc92230](https://github.com/Pelican-Elegant/elegant/commit/cc92230)), closes [#362](https://github.com/Pelican-Elegant/elegant/issues/362)
- **authors:** make authors URL nofollow ([07bf415](https://github.com/Pelican-Elegant/elegant/commit/07bf415))
- **authors:** move authors below share links section ([b81555a](https://github.com/Pelican-Elegant/elegant/commit/b81555a))
- **authors:** open author url in a new window ([f97b47a](https://github.com/Pelican-Elegant/elegant/commit/f97b47a))
- **Chinese:** add better font support for Chinese language ([2711aa0](https://github.com/Pelican-Elegant/elegant/commit/2711aa0)), closes [#134](https://github.com/Pelican-Elegant/elegant/issues/134)
- **modified:** show Last Updated only if the difference between created and modified is more than a day ([b0eac79](https://github.com/Pelican-Elegant/elegant/commit/b0eac79))
- **monetization:** add BestAzon support ([6d8a23c](https://github.com/Pelican-Elegant/elegant/commit/6d8a23c))

# [3.0.0](https://github.com/Pelican-Elegant/elegant/compare/V2.5.0...V3.0.0) (2019-07-03)

### Bug Fixes

- **admonition:** links should inherit the admonition color ([60c9184](https://github.com/Pelican-Elegant/elegant/commit/60c9184))
- **freelists:** use SUBSCRIBE_BUTTON_TITLE instead of generic GO ([c346d1f](https://github.com/Pelican-Elegant/elegant/commit/c346d1f))
- **home:** remove redundant title ([808cd1d](https://github.com/Pelican-Elegant/elegant/commit/808cd1d))

### Features

- **home:** write about me in markdown, reST or AsciiDoc ([9b5b2ec](https://github.com/Pelican-Elegant/elegant/commit/9b5b2ec)), closes [#85](https://github.com/Pelican-Elegant/elegant/issues/85)
- **menu:** set home URL to root if SITEURL is not ([23e0b94](https://github.com/Pelican-Elegant/elegant/commit/23e0b94))

### BREAKING CHANGES

- **home:** Previously LANDING_PAGE_ABOUT was a dictionary that contained html tags. We used it
  to create landing page. But users have demanded from the very beginning to be able to write the
  landing page in markdown. This patch adds this feature. But in order to use it, you have to update
  your configuration.

# [2.5.0](https://github.com/Pelican-Elegant/elegant/compare/V2.4.0...V2.5.0) (2019-06-30)

### Features

- **comments:** replace disqus_identifier with comment_id ([3aa4e24](https://github.com/Pelican-Elegant/elegant/commit/3aa4e24))

# [2.4.0](https://github.com/Pelican-Elegant/elegant/compare/V2.3.0...V2.4.0) (2019-06-30)

### Features

- **footer:** make external links Nofollow ([137a02a](https://github.com/Pelican-Elegant/elegant/commit/137a02a))
- **footer:** move site subtitle to the center ([b5baa11](https://github.com/Pelican-Elegant/elegant/commit/b5baa11))
- **footer:** open exit links in new tab ([8fd9f28](https://github.com/Pelican-Elegant/elegant/commit/8fd9f28))
- **footer:** optionally show the host information ([9de2dab](https://github.com/Pelican-Elegant/elegant/commit/9de2dab))
- **footer:** powered by message is always aligned to the right ([5e47b7c](https://github.com/Pelican-Elegant/elegant/commit/5e47b7c))
- **footer:** remove fixed height by using flexbox for sticky footer ([d9d84e1](https://github.com/Pelican-Elegant/elegant/commit/d9d84e1))
- **footer:** use flexbox instead of list for items in the footer ([bef7db9](https://github.com/Pelican-Elegant/elegant/commit/bef7db9))
- **onelink:** add Amazon Affiliate Disclosure ([cbfa6ac](https://github.com/Pelican-Elegant/elegant/commit/cbfa6ac))

# Version 2.3.0

## Project Management

- Documentation is hosted at https://elegant.oncrashreboot.com/
- Host and build documentation using Netlify
- `elegant.oncrashreboot.com` domain is the final home of documentation. It shall never change
- Delete github pages and related repositories

## Features

- New: FontAwesome updated to version 4.7.0
- New: `Photos` plugin support for photo gallery creation
- New: Lightbox support for `Photos` plugin
- Fixed: Amazon One Link div is in the header
- Fixed: Separated claims for Google and Bing into individual includes

## Documentation

- New: Help article on claim Google and Bing

## CI

- New: Enable deploy previews for every pull request
- New: Add spell check for every pull request, and `master` and `next` branches
- New: Add git hooks to format the code
- New: Add commit Zen support
- New: Add html5validator, which along with w3c_validator, makes for two html validation tools in the CI
- New: Improve CI build times
- Remove: peru for downloading plugins and themes
- New: Add pull request template

# Version 2.2

- New: TipueSearch updated to 7.1
- New: Use `PROJECTS_TITLE` to customize project list title. (default My Projects)
- Changed: Reading Time is displayed only if it is greater than `READING_TIME_LOWER_LIMIT` variable (default 4 min)
- Changed: Project documentation has been moved inside the Elegant repository
- Removed: Google Plus author

# Version 2.0

- Link to your social profiles
- Upgraded to Twitter Bootstrap 2.3.2
- Upgraded to Tipue Search 3.1
- Support for `custom.css`
- [Stat Counter Analytics ](http://statcounter.com/) support
- Google Universal Analytics support
- Support for custom icons for social profiles
- Support for Pelican (>3.3) new metadata `modified`
- Support for Social Media Tags
- Support for Google Authorship
- Translations support
- `article.comments_intro` that overrides `COMMENTS_INTRO`. Now you can define
  article specific comments introduction
- Add Disqus comments to Pages
- All customizable variables consolidated in a single `_defaults.html`, making
  it easier for you to customize or even _localize_ the theme
- Adds author blurbs at the end of the article

## Performance

- Performance improvement- 4x faster output
- Reduce number of HTTP requests using `assets` plugin
- Shortcut icons, like favicon, are disabled by default. Set
  `USE_SHORTCUT_ICONS` to true to enable it

## Visual Style

- Email newsletter subscriber form style matches rest of the theme
- Article images have a visible border
- Block quotes have a quote icon instead of a thick line on left
- Article's paragraph font size is bigger, for better readability
- Remove unnecessary padding in sidebar's tag list
- Archives page and recent posts on home page have better presentation
- Time stamps in categories and tags pages are justified
- Line number in code block is hidden on tablets and phones to save space for
  content
- More sizes of image for Apple Touch icons
- Fixed: Nested lists have different font sizes
- Fixed: CSS style rules for literal block in reST is missing
- Fixed: Long lines in code block will wrap to next line
- Fixed: Code block will not play nice with line numbers
- Fixed: Subscribe button changes its size on smaller screens
- Fixed: Articles under tag heading on tags page are not sorted
- Fixed: URL scheme for blogs which are not published to the root folder
- Fixed: Footer is always under the fold even on smaller length web pages
- Fixed: Site Name and top navigation menu move to left on wide displays
- Fixed: Page link is not active in the navbar if `SAVE_PAGE_AS` is not set to
  default

## Plugins

- Use `neighbor` plugin to show next and previous articles
- Use `assets` plugin to minify CSS and JS files
- Support for `share_post` plugin
- Support for `related_posts` plugin
- Support for `multi_part` plugin
- Support for `post_stats` plugin

## Behaviour

- Search results link open in the same window, which is consistent with
  internet search engines
- Comments section message changes when user toggles it
- Fixed: Clicking Search button in 404.html does not trigger search

# Version 1.3

- Next and previous article navigation is placed below comments section so that article's content and comments appear together
- Article title and site name in `<title>` tag is separated by `·` which is cleaner and more subtle than `-`
- Subtitle of articles and pages is added in `<title>` tag along with main title
- Description meta tag on Home Page uses `SITE_DESCRIPTION`
- Bug fix: Expand comments section if URL points to a comment
- Bug fix: CSS style of links in an unordered list inside article content is different from article links

# Version 1.2

- RSS and Atom feed links
- CSS style for permanent links added. It is visible only user hovers over the heading
- Block quote is indented towards left
- Bug fix: Hyperlink dashed underline is not visible on Chrome
- Bug fix: Text in list goes beyond list marker when text is long and overflows to next line
- Bug fix: Disqus comment count is always 0

# Version 1.1

- Add template for pages. Pages do not have tags, category and Disqus comments
- Keep style of a hyperlink in `modified` meta data consisted with the theme
- Add `keywords` meta tag that uses keywords, tags and category attribute of articles and pages
- Validate search form for empty strings
- If `RECENT_ARTICLES_COUNT` is undefined, set it to 10. So that Pelican does not throw critical error
- Bug fix: Path of search.html in search form action should always be absolute
- Bug fix: Copyright meta tag should be set to the author, instead of the license
- Bug fix: Close meta tags
- Bug fix: ID of search form in 404 page should be different from the ID of search form in main navigation
- Bug fix: Links in ordered list in an article do not conform to the link style in rest of the article

# Version 1.0

- Initial release
