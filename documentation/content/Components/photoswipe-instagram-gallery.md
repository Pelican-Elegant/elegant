---
Title: Gallery -- Use Instagram
authors: Talha Mansoor, Pablo Iranzo Gómez
Tags: nuances, images, gallery, instagram
Date: 2020-02-06
Slug: photoswipe-gallery-using-instagram
Category: Components
---

Similar to the use case defined in [Photogallery]({filename}photoswipe-raw-gallery.md), Pelican-Elegant has code in place for showing Instagram galleries.

## Article contents

To embed Instagram gallery, just define a div in this manner,

```yaml
## Multiple image
<div class="elegant-instagram" data-instagram-id="BwWo35fAcR3"></div>

## Single image

<div class="elegant-instagram" data-instagram-id="B7yh4IdItNd"></div>
```

For reference, the `data-instagram-id` is taken from Instagram picture URL, for example:

`https://www.instagram.com/p/OzF8OwS43q/` will mean adding to the div the parameter `data-instagram-id=OzF8OwS43q`.

!!! hint "`data-instagram-id` defines either picture or set of pictures"

    Note that `data-instagram-id` is the part in the url of a post, that can be a single or multiple pictures 'post' and in both case the library will show them.

!!! danger "`class=elegant-instagram` class"

    Note that `<div>`class must be `elegant-instagram` for the code to work properly, do not change it.

The above `article` code will then render as this:

## Multiple images

<div class="elegant-instagram" data-instagram-id="BwWo35fAcR3"></div>

## Single image

<div class="elegant-instagram" data-instagram-id="B7yh4IdItNd"></div>
