---
Title: Add Author Blurbs to Your Articles
Tags: pelican-theme, web-design
Category: Elegant - Pelican Theme
Date: 2018-12-07 11:00
Slug: adding-author-blurbs
Disqus_identifier: c8et6bu-adding-author-blurbs
Subtitle:
Summary: Elegant can be configured to provide author blurbs for articles, relaying extra information on the authors of the articles.
Keywords:
Authors: Talha Mansoor, Jack De Winter
---

[TOC]

On websites where the author of an article may vary, many sites include a quick blurb about
the author with the article.  This blurb will typically be at the start of the article or the
end of the article, and provides extra information for readers on the author.  Elegant provides
this feature, adding a section for any recognized articles at the end of the article.

Here are two examples of what the Author Blurbs may look like:

![Author Blurb 1]({static}/images/author-blurb.png)

![Author Blurb 2]({static}/images/author-blurb2.png)

## Configuration

To enable author blurbs for your articles, you need to add an `AUTHORS` configuration variable
to your pelican configuration.  The `AUTHORS` configuration variable for the Elegant
documentation website is specified as follows:

```python
AUTHORS = {
    "Talha Mansoor": {
        "url": "https://www.oncrashreboot.com/",
        "blurb": "is the creator and lead developer of Elegant theme.",
        "avatar": "/images/avatars/talha131.png",
    },
    "Pablo Iranzo Gómez": {
        "url": "http://iranzo.github.io",
        "blurb": " opensource enthusiast and Lego fan doing some python simple programs like @redken_bot in telegram, etc",
        "avatar": "https://avatars.githubusercontent.com/u/312463",
    },
    "Jack De Winter": {
        "url": "http://jackdewinter.github.io",
        "blurb": "ever evolving, ever learning",
    },
}
```

The value assigned to the configuration variable is a Python dictionary[^PythonDictionary]
containing one key-value pair for every author.  The key for the key-value pair is the name of
the author as you want it to appear at the end of the article.  In the our example, the three
authors are "Tahla Mansoor", "Pablo Iranzo Gómez", and "Jack De Winter".

[^PythonDictionary]: For more information on Python dictionaries, refer to this comprehensive article on [Python dictionaries](https://realpython.com/python-dicts/).

The value for each of the key-value pairs is it's own dictionary.  Elegant specifically looks
for three keys in the each author's dictionary:

- `url` (string) URL to the author's homepage or profile
- `blurb` (string) Introduction of author
- `avatar` (string) URL to author's avatar image

For the `url` and `avatar` values, there is no restriction on where the URL resides.  In the
Elegant documentation example above, Tahla's URLs are both local, while Pablo's URLs are both
remote.

## Article Metadata

While the configuration for Author Blurbs is centralized in the configuration file, enabling
this feature for a given article requires that the article contains either the `author` or
`authors` [metadata]({static}/Extra&#32;Customization/meta-data.md) field values.  If neither
of these values are provided, the `AUTHOR` configuration variable will be used as a default.

```Python
AUTHOR = 'Pablo Iranzo Gómez'
```

The default `AUTHOR` configuration variable and the `author` metadata field are both denote a
single author.  The `authors` metadata field denotes multiple authors using a comma separated
list.

For each author determined through in this manner, a check is performed against the `AUTHORS`
configuration in the previous section on [Configuration](#Configuration).  If the author is
found using a case-sensitive exact match, a blurb will be generated for that author. If the
author is not found, it will be silently ignored.

A good example of the `authors` metadata field is available by looking at the
[raw Markdown](https://raw.githubusercontent.com/Pelican-Elegant/elegant/master/documentation/content/Elegant%20-%20Pelican%20Theme/author-blurbs.md) for this page.

!!! warning
    A frequent mistake is to define multiple authors, but assign the value to the `author` metadata field.  This can happen easily if one author writes the original version of the article and another author updates or changes that article.  This mistake causes Elegant to look for that *single* author using the entire text for that value.  The correct way to do this is to use `authors` metadata field.
