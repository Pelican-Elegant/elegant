---
Title: Creating a Photo Gallery Article from Instagram post
Tags: pelican-theme, pelican-plugin, photo gallery, instagram, galleriaio
Category: Supported Plugins
Date: 2020-01-27 17:40
Slug: how-to-use-galleriaio-plugin
Subtitle:
Summary: Elegant can be configured to provide a simple display of pictures.
Keywords: photos, gallery, photogallery, instagram, galleriaio
Authors: Pablo Iranzo Gómez
instagram_id: B3ePmL7gd1P
---

[TOC]

Similar to the use case defined in [Photogallery]({filename}photogallery.md), Pelican uses <https://galleria.io> code to show images from instagram.

## Article Metadata

To enable the plugin, just set a `yaml preamble` entry for instagram like:

```yaml
instagram_id: <picture ID>
```

For reference, the `picture ID` is taken from Instagram picture URL, for example:

`https://www.instagram.com/p/OzF8OwS43q/` will mean adding to the headers:

```yaml
instagram_id: OzF8OwS43q
```

To get it shown on the article.

No other plugin settings must be configured or modified at this time.

!!! hint "instagram_id defines either picture or set of pictures"

    Note that `instagram_id` is the part in the url of a post, that can be a single or multiple pictures 'post' and in both case the library will show them.
