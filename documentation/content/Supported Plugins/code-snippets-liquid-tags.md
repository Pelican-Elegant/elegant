---
Title: Code Snippets -- Include code from file
Tags: code-snippets, plugins, liquid-tags
Date: 2020-02-02 20:53
comments: false
Slug: code-snippets-include-code-from-file
authors: Talha Mansoor
Category: Supported Plugins
---

Elegant supports [`liquid_tags.include_code` plugin](https://github.com/getpelican/pelican-plugins/tree/master/liquid_tags#include-code).

<!-- TODO: remove this warning after https://github.com/getpelican/pelican-plugins/pull/1243 is merged -->

!!! Warning "Pending Pull Request"

    The demo you see here is dependent on [this
    patch](https://github.com/getpelican/pelican-plugins/pull/1243).

    Until Pelican team merges the patch into plugins repository, you will have
    apply this patch manually to your copy of plugins.

## Example 1

{% include_code square-root.py lang:python Calculate square root of 8 %}<!-- yaspeller ignore -->

## Example 2 -- Without Filename

{% include_code alias-sed.fish :hidefilename: Fish Shell alias for sed %}<!-- yaspeller ignore -->

## Example 3 -- Without Download Link

{% include_code alias-sed.fish :hidelink: Fish Shell alias for sed %}<!-- yaspeller ignore -->

## Example 4 -- Without Filename and Download Link

{% include_code alias-sed.fish :hidefilename: :hidelink: Fish Shell alias for sed %}<!-- yaspeller ignore -->

## Example 5 -- Without Metadata

{% include_code square-root.js lang:js :hideall: Compute square-root %}<!-- yaspeller ignore -->
