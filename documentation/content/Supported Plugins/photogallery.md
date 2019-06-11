Title: Photo gallery plugin
Tags: pelican-theme, pelican-plugin, photo-gallery
Category: Supported Plugins
Date: 2019-06-09 10:49
Slug: how-to-use-photos-plugin
Subtitle:
Summary: Elegant integrates 'photos' gallery plugin of Pelican  out of the box
Keywords: photos, gallery, photogallery

In order to easily work with Photos, Pelican has a plugin for [photos](https://github.com/getpelican/pelican-plugins/tree/master/photos) that allows to easily show folders of pictures inside an article.

The relevant template for article has been already incorporated in Pelican, so last steps are to add to you requirements the ones for this plugin `Pillow` and optionally `Piexif`.


## Setup

Elegant supports it out of the box. You just have to enable it in your Pelican
configuration,

    :::python
    PLUGINS = ['photos']

Refer to the plugin documentation for configuration, but at the time of this writing, the settings are:

`PHOTO_LIBRARY = "~/Pictures"`
:	Absolute path to the folder where the original photos are kept, organized in sub-folders.

`PHOTO_GALLERY = (1024, 768, 80)`
:	For photos in galleries, maximum width and height, plus JPEG quality as a percentage. This would typically be the size of the photo displayed when the reader clicks a thumbnail.

`PHOTO_ARTICLE = (760, 506, 80)`
:	For photos associated with articles, maximum width, height, and quality. The maximum size would typically depend on the needs of the theme. 760px is suitable for the theme `notmyidea`.

`PHOTO_THUMB = (192, 144, 60)`
:	For thumbnails, maximum width, height, and quality.

`PHOTO_SQUARE_THUMB = False`
:	Crops thumbnails to make them square.

`PHOTO_RESIZE_JOBS = 5`
: Number of parallel resize jobs to be run. Defaults to 1.

`PHOTO_WATERMARK = True`
: Adds a watermark to all photos in articles and pages. Defaults to using your site name.

`PHOTO_WATERMARK_TEXT' = SITENAME`
: Allow the user to change the watermark text or remove it completely. By default it uses [SourceCodePro-Bold](http://www.adobe.com/products/type/font-information/source-code-pro-readme.html) as the font.

`PHOTO_WATERMARK_IMG = ''`
: Allows the user to add an image in addition to or as the only watermark. Set the variable to the location.

**The following features require the piexif library**
`PHOTO_EXIF_KEEP = True`
: Keeps the exif of the input photo.

`PHOTO_EXIF_REMOVE_GPS = True`
: Removes any GPS information from the files exif data.

`PHOTO_EXIF_COPYRIGHT = 'COPYRIGHT'`
: Attaches an author and a license to the file. Choices include:
	- `COPYRIGHT`: Copyright
	- `CC0`: Public Domain
	- `CC-BY-NC-ND`: Creative Commons Attribution-NonCommercial-NoDerivatives
	- `CC-BY-NC-SA`: Creative Commons Attribution-NonCommercial-ShareAlike
	- `CC-BY`: Creative Commons Attribution
	- `CC-BY-SA`: Creative Commons Attribution-ShareAlike
	- `CC-BY-NC`: Creative Commons Attribution-NonCommercial
	- `CC-BY-ND`: Creative Commons Attribution-NoDerivatives

`PHOTO_EXIF_COPYRIGHT_AUTHOR = 'Your Name Here'`
: Adds an author name to the photo's exif and copyright statement. Defaults to `AUTHOR` value from the `pelicanconf.py`

## How to use it in your articles

In order to use it, in your `YAML` preamble of articles, add a line like this:

`gallery: {filename}gallery-source/foldername`

In order for the plugin to work, place your pictures in the folder defined by `PHOTO_LIBRARY`, for example:
`~/www/content/gallery-source/foldername`

The `photos` plugin will process the images, resize, include the watermark, etc and store in the output folder. Images will only be reprocessed if those are removed from the `output` folder, this allows to save time when processing big galleries.

This is an example of the final result:

![]({static}../images/photogallery.png)
