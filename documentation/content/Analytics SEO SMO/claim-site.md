---
Title: Claim website on Google and Bing
Tags: google, bing, crawler
Category: Analytics, SEO and SMO
Date: 2019-06-27
Slug: website-claim
Comment_id: hk9m5eq-website-claim
Subtitle:
Summary: Easily insert headers to claim website
Keywords:
---

For submitting a website and sitemap to Google Search Console or Bing Webmaster tools
we've to consider some steps.

One of those steps is to claim the website ownership.

Several approaches are available:

- Create a specific file on the root folder of the website
- Use a DNS Record
- Insert a `<meta>` TAG in pages to claim it.

Usually both DNS record or uploading files make things more complicated
(require DNS setup, or configure pelican to upload static file to path,
etc).

Pelican-Elegant has simplified this by including support for the `<meta>` TAG
being inserted if the values are defined in pelicanconf.

Use the following variables to insert the relevant `<meta>` in the document
headers:

- `CLAIM_GOOGLE`
- `CLAIM_BING`

Each one of those should be filled according to the values provided by
Google/Bing on their respective websites for webmasters:

- [Google Search Console](https://www.google.com/webmasters/tools/dashboard?pli=1)
- [Bing Webmaster tools](https://www.bing.com/webmaster/configure/verify/ownership)

Once configured and when site is regenerated, the header should be there.
