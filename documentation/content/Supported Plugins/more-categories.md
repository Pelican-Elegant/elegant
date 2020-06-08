---
Title: Articles with multiple categories
Tags: pelican-plugin, more-categories
Category: Supported Plugins
Date: 2020-06-02 10:14
Slug: articles-with-multiple-categories
Subtitle:
Summary: You can have articles with multiple categories
Keywords: categories
Authors: David García Garzón
---

Both tags and categories fulfil the purpose of relating your
by a subject or a kind of writing.
Tags are more open and free and
you can attach several of them to a single article.
Categories are a more closed set, they are
used to organize your writings in classes
and you can only attach one category to every single article.

Depending on how you organize you website it might have sense
for an article to be in more than one category
and overcome that later restriction on categories.
The `more-categories` plugin fulfils this purpose
and enables multiple categories.

Besides `more-categories` enables hierarchies of categories.
You might have a `Sports` category, and then
a sub category talking about `Basketball`.
So you will be talking about `Sports/Basketball`.
Your articles about Basketball will be also
included when you look at the Sports category.

This is also useful to have a kind of [Trove classifiers](https://pypi.org/classifiers/).

When you specify several categories, Elegant will show you all
the categories an article is in.

![Recent Post List]({static}/images/elegant-theme-more-categories-plugin-recent-post.png)

![Article Side Info]({static}/images/elegant-theme-more-categories-plugin-side-info.png)


## Configuration

Just include the plugin in the configuration by adding:

```bash
$ pip install pelican-more-categories
```

```python
PLUGINS = [
	...
	'pelican.plugin.more_categories',
	...
]
```

## Article Metadata

And then add several categories to an article by
using commas to separate them in the metadata:

```markdown
Category: One Category, Other Category, One Category/A subcategory
```

