---
Authors: Jack De Winter
Title: Add A Reading Time Estimate to Your Articles
Tags: reading time
Date: 2019-07-15 20:08
Slug: reading-time-estimate
Summary: Elegant can be configured to provide an estimate of the reading time for your articles, giving the user the ability to gauge how long the articles are.
Category: Supported Plugins
---

When you go to articles on a number of popular websites, the articles will present an estimate
to the reader on the amount of time it will take to read the article. This estimate is
typically based on the average reading speed of an adult being roughly 265 words per minute
while retaining comprehension. Elegant provides this feature, adding a `Reading Time` section
at the top of the text on the right side of the article with the estimate for the current
article.

Here is an example of what the Reading Time estimate may look like:

![Reading Time Section]({static}/images/elegant-theme_reading-time.png)

## Configuration

To enable the reading time for your articles, you need to add `post_stats` to `PLUGINS` in
your pelican configuration.

```python
PLUGINS = ['post_stats']
```

Note that these values must be added to any existing values present for the `PLUGINS`
configuration variables.

In addition, the `READING_TIME_LOWER_LIMIT` configuration variable can be set to specify a
lower limit for this feature. If not supplied, the default value for this variable is 4.

If the estimated reading time is less than or equal to this value, the Reading Time section
will not be included for the article. Given the default of 4 for this variable, this section
will only be visible for articles that have an estimated reading time of 5 minutes or more.
