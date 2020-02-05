---
Title: Creating a Photo Gallery Article from Instagram post
Tags: pelican-theme, pelican-plugin, photo gallery, instagram
Category: Supported Plugins
Date: 2020-01-27 17:40
Slug: how to use the instrgram plugin
Subtitle:
Summary: Elegant can be configured to provide a simple display of pictures.
Keywords: photos, gallery, photogallery, instagram
Authors: Pablo Iranzo Gómez
---

[TOC]

Similar to the use case defined in [Photogallery]({filename}photogallery.md), Pelican has code in place for showing instragram galleries.

## Article contents

To enable the plugin, just define a similar div inside your article for each gallery:

```yaml
---
author: Pablo Iranzo Gómez
title: Instagram
tags: python, redken, descuenbot, deal, chollo, bargain, rabbate, soldes
date: 2020-01-27 00:35:00 +0100
comments: true
category: blog
description:
lang: en
---
Before div

<div id="photoswipe-instagram" class="photoswipe-gallery" data-gallery-id="BwWo35fAcR3" itemscope itemtype="http://schema.org/ImageGallery">
<div></div>
</div>
After div

<div id="photoswipe-instagram" class="photoswipe-gallery" data-gallery-id="B71YHQ6DugB" itemscope itemtype="http://schema.org/ImageGallery">
<div></div>
</div>
```

For reference, the `data-gallery-id` is taken from Instagram picture URL, for example:

`https://www.instagram.com/p/OzF8OwS43q/` will mean adding to the div the parameter `data-gallery-id=OzF8OwS43q`.

To get it shown on the article.

No other plugin settings must be configured or modified at this time.

!!! hint "data-gallery-id defines either picture or set of pictures"

    Note that `data-gallery-id` is the part in the url of a post, that can be a single or multiple pictures 'post' and in both case the library will show them.
