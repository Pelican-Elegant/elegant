---
author: Pablo Iranzo Gómez
title: Pelican-Elegant and RevealMD presentations
tags: pelican, foss, blog, python, github, blog-o-matic, Linux, pandoc
date: 2019-07-22 22:12:17 +0100
comments: true
category: Supported Plugins
slug: reveal-md-presentations-in-elegant.
---

[TOC]

## Introduction

Pelican allows several plugins, and one of them allows rendering of RevealMD presentations into web pages that can
be served as part of your blog, in this way, both your blog content and
slides can be served from your server.

In order to enable the processing and rendering, a new plugin needs to be
added to your Pelican-Elegant installation, named 'pelican-revealmd'.

Pelican-revealmd uses `pandoc` binary under the hood to do the actual
conversion (and yes, as there's a 'conversion', it means that some features
in your slides might be lost).

### Issues

You can find more details on the [initial issues found](https://iranzo.github.io/blog/2019/01/20/pelican-revealjs/)
and how they were fixed.

## Usage

- Enable pelican-revealmd plugin from this repository: <https://github.com/iranzo/pelican-revealmd>
- Create your revealMD files and name them as 'revealjs' (files are regular Markdown 'revealmd' presentations, just named as `.revealjs`), for example `my_presentation.revealjs`
- Enable `revealmd` in your `pelicanconf.py` and ensure that pandoc and its dependencies are installed

## How does it looks like?

Well, one of my examples is the [blog-o-matic
presentation](https://iranzo.github.io/blog/2019/01/16/automate-project-github-pages-travis-and-quay/#/title-slide),
which, also (blog-o-matic) is enabled for rendering 'out of the box' your
slides.
