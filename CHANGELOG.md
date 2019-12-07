# [5.1.0](https://github.com/Pelican-Elegant/elegant/compare/V5.0.1...V5.1.0) (2019-12-05)

### Bug Fixes

- **applause:** applause_button tag does not auto close ([d37e691](https://github.com/Pelican-Elegant/elegant/commit/d37e691e0592bded8dd42531ceacfa61147ad078))
- **typography:** make headings align to the left instead of justify ([101285e](https://github.com/Pelican-Elegant/elegant/commit/101285e0884ea365e9e3272e6f914fe373fa27fb))

### Features

- **applause:** add option to set applause_button_id ([8eda9a4](https://github.com/Pelican-Elegant/elegant/commit/8eda9a4cc7c588ff09a520e9f7fa183d1fb11031))
- **applause:** add support for applause button ([e4872fd](https://github.com/Pelican-Elegant/elegant/commit/e4872fd558964c3007c516fc616314c88de49eef)), closes [#532](https://github.com/Pelican-Elegant/elegant/issues/532)
- **applause:** simplify filter option ([9f8b60f](https://github.com/Pelican-Elegant/elegant/commit/9f8b60fc3cbc08e7e21cef08f7e44658131677dd))

## [5.0.1](https://github.com/Pelican-Elegant/elegant/compare/V5.0.0...V5.0.1) (2019-12-04)

### Bug Fixes

- **blockquote:** close quote is not aligned properly ([80a85c7](https://github.com/Pelican-Elegant/elegant/commit/80a85c714a16cd01c53831347ac1f18b397dda1a))
- **typography:** remove unit from line height ([10286a1](https://github.com/Pelican-Elegant/elegant/commit/10286a13fade3248cc752a3ac5416257920d07bf))

# [5.0.0](https://github.com/Pelican-Elegant/elegant/compare/V4.0.0...V5.0.0) (2019-12-02)

### Bug Fixes

- **css:** linter warning ([a5f5c81](https://github.com/Pelican-Elegant/elegant/commit/a5f5c8170a61683edf5737918b7fe3cae1b67c00))
- **page:** social profiles appear in the sidebar ([c17077c](https://github.com/Pelican-Elegant/elegant/commit/c17077cbd24811bb91e48610ac13d76328e5398d)), closes [#534](https://github.com/Pelican-Elegant/elegant/issues/534)
- **social:** reduce icon size in the sidebar ([4e0dc41](https://github.com/Pelican-Elegant/elegant/commit/4e0dc415c114bb07304605c9b1c153e372f1fa4b)), closes [#490](https://github.com/Pelican-Elegant/elegant/issues/490)
- **typography:** adjust heading sizes and set small font-style to italic ([d3bbf04](https://github.com/Pelican-Elegant/elegant/commit/d3bbf04eabcd89bdb2f039b11fac7a6150729e90))
- **typography:** remove border from headings in archive page ([817bea8](https://github.com/Pelican-Elegant/elegant/commit/817bea8d091e99b6d6e5fc3dcc63ba6f627c5b66))

### Features

- **blockquote:** improve blockquote look ([068d50a](https://github.com/Pelican-Elegant/elegant/commit/068d50a455d57e4706525908b174bbc4606c6fb6))
- **border:** change border radius of tags and code blocks to match rest of the theme ([5d0285f](https://github.com/Pelican-Elegant/elegant/commit/5d0285f156a5da734b438868674c632b897625ef)), closes [#521](https://github.com/Pelican-Elegant/elegant/issues/521)
- **border:** have consistent border radius ([7307467](https://github.com/Pelican-Elegant/elegant/commit/7307467579d4ab1931987e48b83224eb666e9e5e)), closes [#521](https://github.com/Pelican-Elegant/elegant/issues/521)
- **code-block:** minor refine code-block style ([2ba2232](https://github.com/Pelican-Elegant/elegant/commit/2ba22321b35961ebc18dbb2c25f1db535fad64ed))
- **css:** use PostCSS for processing CSS files ([2b88865](https://github.com/Pelican-Elegant/elegant/commit/2b88865a36780257ac42173b949b5d7b4df516e9)), closes [#354](https://github.com/Pelican-Elegant/elegant/issues/354)
- **links:** add new style and improve existing style for hyperlinks ([87fd3d3](https://github.com/Pelican-Elegant/elegant/commit/87fd3d3f88cebac83ca04460ef41e7356df0ccd2)), closes [#533](https://github.com/Pelican-Elegant/elegant/issues/533) [#519](https://github.com/Pelican-Elegant/elegant/issues/519)
- **permalink:** improve permalink look ([8059ca8](https://github.com/Pelican-Elegant/elegant/commit/8059ca84b77ab82bffd1ed80f010235f9ca57ed6))
- **security:** use rel="noopener noreferrer" with all target="\_blank" ([4c843e9](https://github.com/Pelican-Elegant/elegant/commit/4c843e9a0c66bb2656ef5df4411d4c891c493a11))
- **typography:** code inside heading is consistently 80% of the size ([7180b49](https://github.com/Pelican-Elegant/elegant/commit/7180b49ebb659d00a82f10769269e6236057e42c)), closes [#508](https://github.com/Pelican-Elegant/elegant/issues/508)
- **typography:** headings sizes and other properties are consistent ([afa99ab](https://github.com/Pelican-Elegant/elegant/commit/afa99ab89baf715a68627552152b7163ea0534b9)), closes [#508](https://github.com/Pelican-Elegant/elegant/issues/508) [#521](https://github.com/Pelican-Elegant/elegant/issues/521)
- **typography:** use darker color for article heading and increase border size ([1922075](https://github.com/Pelican-Elegant/elegant/commit/19220758aabf431ae3566b950436fe04a3ee21a8))

### BREAKING CHANGES

- **links:** Style of muted links have been changed slightly. It is
  still muted but has modern animation.

# [4.0.0](https://github.com/Pelican-Elegant/elegant/compare/V3.2.0...V4.0.0) (2019-08-22)

### Bug Fixes

- **admonition:** an artifact in border behind the title ([88113c3](https://github.com/Pelican-Elegant/elegant/commit/88113c3))
- **admonition:** reduce border radius to match radii of other components ([de08d20](https://github.com/Pelican-Elegant/elegant/commit/de08d20)), closes [#490](https://github.com/Pelican-Elegant/elegant/issues/490)
- **admonition:** remove box shadow ([d059db8](https://github.com/Pelican-Elegant/elegant/commit/d059db8)), closes [#490](https://github.com/Pelican-Elegant/elegant/issues/490)
- **admonition:** remove text-shadow from heading ([1c889da](https://github.com/Pelican-Elegant/elegant/commit/1c889da)), closes [#490](https://github.com/Pelican-Elegant/elegant/issues/490)
- **clean URL:** default URL of categories, tags and archives fails on some servers ([3c7df6a](https://github.com/Pelican-Elegant/elegant/commit/3c7df6a)), closes [#280](https://github.com/Pelican-Elegant/elegant/issues/280) [#276](https://github.com/Pelican-Elegant/elegant/issues/276)
- **comments:** W3C validation errors ([76a1f26](https://github.com/Pelican-Elegant/elegant/commit/76a1f26))
- **disqus:** remove SITEURL condition to show Disqus comments section ([753d5a5](https://github.com/Pelican-Elegant/elegant/commit/753d5a5))
- **lang:** do not override default value of DEFAULT_LANG set by Pelican ([d6c60c2](https://github.com/Pelican-Elegant/elegant/commit/d6c60c2)) <!-- yaspeller ignore -->
- **social:** reduce icon sizes in the sidebar ([c769ba3](https://github.com/Pelican-Elegant/elegant/commit/c769ba3))
- **social:** use nofollow for social links in the sidebar ([50cff87](https://github.com/Pelican-Elegant/elegant/commit/50cff87))
- **social:** W3C validation error ([ec4521e](https://github.com/Pelican-Elegant/elegant/commit/ec4521e))
- **table:** reduce border radius to match radii of other components ([7eaaa96](https://github.com/Pelican-Elegant/elegant/commit/7eaaa96))
- **w3c validation:** remove incorrect usage of article tag ([e8231e0](https://github.com/Pelican-Elegant/elegant/commit/e8231e0)), closes [#251](https://github.com/Pelican-Elegant/elegant/issues/251)
- **w3c validation:** remove obsolete charset attribute ([8deb285](https://github.com/Pelican-Elegant/elegant/commit/8deb285)), closes [#251](https://github.com/Pelican-Elegant/elegant/issues/251)
- **w3c validation:** remove redundant article tag ([d07c27e](https://github.com/Pelican-Elegant/elegant/commit/d07c27e)), closes [#251](https://github.com/Pelican-Elegant/elegant/issues/251)
- **w3c validation:** remove redundant sections without heading ([df9221f](https://github.com/Pelican-Elegant/elegant/commit/df9221f)), closes [#251](https://github.com/Pelican-Elegant/elegant/issues/251)
- **w3c validation:** remove type and language attributes ([b700224](https://github.com/Pelican-Elegant/elegant/commit/b700224)), closes [#251](https://github.com/Pelican-Elegant/elegant/issues/251)
- **w3c validation:** update CSS rules ([0b78d46](https://github.com/Pelican-Elegant/elegant/commit/0b78d46)), closes [#251](https://github.com/Pelican-Elegant/elegant/issues/251)

### Features

- **404:** auto fill search box with URL fragment that was not found ([c0a7f47](https://github.com/Pelican-Elegant/elegant/commit/c0a7f47))
- **admonition:** add box shadow ([246f826](https://github.com/Pelican-Elegant/elegant/commit/246f826))
- **admonition:** border color should match the title color ([1adadbe](https://github.com/Pelican-Elegant/elegant/commit/1adadbe))
- **admonition:** increase contrast of title ([7fb82cc](https://github.com/Pelican-Elegant/elegant/commit/7fb82cc))
- **admonition:** use svg image instead of font-awesome icon ([e7c4029](https://github.com/Pelican-Elegant/elegant/commit/e7c4029)), closes [#487](https://github.com/Pelican-Elegant/elegant/issues/487) <!-- yaspeller ignore -->
- **clean url:** support clean URL for search page ([088791e](https://github.com/Pelican-Elegant/elegant/commit/088791e))
- **comments:** add support for utterances comment system ([a2151cc](https://github.com/Pelican-Elegant/elegant/commit/a2151cc)), closes [#288](https://github.com/Pelican-Elegant/elegant/issues/288)
- **quotes:** improve style and remove font-awesome for quote icon ([9ef3ac8](https://github.com/Pelican-Elegant/elegant/commit/9ef3ac8)), closes [#487](https://github.com/Pelican-Elegant/elegant/issues/487)
- **social:** add icons for 7 more websites ([8dcf8fa](https://github.com/Pelican-Elegant/elegant/commit/8dcf8fa)), closes [#494](https://github.com/Pelican-Elegant/elegant/issues/494)
- **social:** use svg icons instead of font-awesome ([19f458b](https://github.com/Pelican-Elegant/elegant/commit/19f458b)) <!-- yaspeller ignore -->
- **table:** add style rule to make tables pop out ([6a8500b](https://github.com/Pelican-Elegant/elegant/commit/6a8500b)), closes [#440](https://github.com/Pelican-Elegant/elegant/issues/440)

### Performance Improvements

- **admonition:** add attributes to svg images ([a740a60](https://github.com/Pelican-Elegant/elegant/commit/a740a60)) <!-- yaspeller ignore -->
- **requests:** remove font awesome ([7c20145](https://github.com/Pelican-Elegant/elegant/commit/7c20145)), closes [#487](https://github.com/Pelican-Elegant/elegant/issues/487)

### BREAKING CHANGES

- **requests:** We have removed font awesome. Now we use svg images for all icons. This will result in one less web request, which in turn will improve your websites performance. <!-- yaspeller ignore -->
- **social:** Style customization and configuration of social icons
  in the sidebar has changed.

New icons have better colors and bigger sizes.

- **clean URL:** To enable clean URLs for tags, categories and archives,
  first configure your server to support clean URLs. Then set `TAGS_URL`,
  `CATEGORIES_URL` and `ARCHIVES_URL` to `"tags"`, `"categories"` and
  `"archives"` respectively.

# [3.2.0](https://github.com/Pelican-Elegant/elegant/compare/V3.1.0...V3.2.0) (2019-07-30)

### Bug Fixes

- **freelists:** open FreeLists subscription form in a new tab ([f81657c](https://github.com/Pelican-Elegant/elegant/commit/f81657c)) <!-- yaspeller ignore -->
- **freelists:** replace deprecated subscription form with button ([9bfe3c1](https://github.com/Pelican-Elegant/elegant/commit/9bfe3c1)), closes [#412](https://github.com/Pelican-Elegant/elegant/issues/412)
- **freelists:** remove unused include ([27f0831](https://github.com/Pelican-Elegant/elegant/commit/27f0831))

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
- **footer:** remove fixed height by using flexbox for sticky footer ([d9d84e1](https://github.com/Pelican-Elegant/elegant/commit/d9d84e1)) <!-- yaspeller ignore -->
- **footer:** use flexbox instead of list for items in the footer ([bef7db9](https://github.com/Pelican-Elegant/elegant/commit/bef7db9)) <!-- yaspeller ignore -->
- **onelink:** add Amazon Affiliate Disclosure ([cbfa6ac](https://github.com/Pelican-Elegant/elegant/commit/cbfa6ac))

# Version 2.3.0

## Project Management

- Documentation is hosted at https://elegant.oncrashreboot.com/
- Host and build documentation using Netlify
- `elegant.oncrashreboot.com` domain is the final home of documentation. It shall never change
- Delete github pages and related repositories

## Features

- New: FontAwesome updated to version 4.7.0 <!-- yaspeller ignore -->
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
- Description metadata tag on Home Page uses `SITE_DESCRIPTION`
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
- Keep style of a hyperlink in `modified` metadata consisted with the theme
- Add `keywords` metadata tag that uses keywords, tags and category attribute of articles and pages
- Validate search form for empty strings
- If `RECENT_ARTICLES_COUNT` is undefined, set it to 10. So that Pelican does not throw critical error
- Bug fix: Path of search.html in search form action should always be absolute
- Bug fix: Copyright metadata tag should be set to the author, instead of the license
- Bug fix: Close metadata tags
- Bug fix: ID of search form in 404 page should be different from the ID of search form in main navigation
- Bug fix: Links in ordered list in an article do not conform to the link style in rest of the article

# Version 1.0

- Initial release
