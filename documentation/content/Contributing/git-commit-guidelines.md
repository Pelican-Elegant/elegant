---
Title: Git Commit Guidelines
Subtitle: Mandatory
Date: 2019-07-20 23:17
Slug: git-commit-guidelines
Category: Contributing
Authors: Talha Mansoor
---

[TOC]

Elegant release process is [fully automated]({filename}./automated-release.md). It only works if all commit messages adhere to the set rules.

Why?

> semantic-release uses the commit messages to determine the type of changes in the codebase. Following formalized conventions for commit messages, semantic-release automatically determines the next semantic version number, generates a changelog and publishes the release.

Basically, semantic-release goes through the commit messages, parses them and on its bases makes the decisions of publishing new release and new version number.

What are those rules?

Elegant development team chose to use [Angular Commit Message Conventions](https://github.com/angular/angular.js/blob/master/DEVELOPERS.md#-git-commit-guidelines).

Following portion is largely derived from their [guidelines](https://gist.github.com/stephenparish/9941e89d80e2bc58a153).

!!! Tip "Use Commitizen"

    Reading, understanding and then getting used to following guidelines may take sometime.

    Make your life easier and [use Commitizen for Git commits]({filename}./commitizen.md).
    It automatically formats the commit message to conform to our guidelines.

## Commit Message Format

Each commit message consists of a **header**, a **body** and a **footer**. The header has a special
format that includes a **type**, a **scope** and a **subject**:

```text
<type>(<scope>): <subject>
<BLANK LINE>
<body>
<BLANK LINE>
<footer>
```

The **header** is mandatory and the **scope** of the header is optional.

Any line of the commit message cannot be longer 100 characters! This allows the message to be easier
to read on GitHub as well as in various git tools.

## Header

### Revert Commits

If the commit reverts a previous commit, it should begin with `revert:`, followed by the header
of the reverted commit.
In the body it should say: `This reverts commit <hash>.`, where the hash is the SHA of the commit
being reverted.

### Type

Must be one of the following:

- **feat**: A new feature
- **fix**: A bug fix
- **docs**: Documentation only changes
- **style**: Changes that do not affect the meaning of the code (white-space, formatting, missing
  semi-colons, etc)
- **refactor**: A code change that neither fixes a bug nor adds a feature
- **perf**: A code change that improves performance <!-- yaspeller ignore -->
- **test**: Adding missing or correcting existing tests
- **chore**: Changes to the build process or auxiliary tools and libraries such as documentation
  generation

### Scope

The scope could be anything specifying place of the commit change. For example, `authors` if the change is about Elegant [authors blurb]({filename}../Supported Plugins/author-blurbs.md) feature or `home` if it refers to [landing page]({filename}../Landing Page/landing-page.md).

## Subject Text

1.  use imperative, present tense: "change" not "changed" nor "changes" not "changing"
1.  don't capitalize first letter
1.  no dot (.) at the end

### What is Imperative mode

[Here](https://chris.beams.io/posts/git-commit/#imperative) is a very good explanation of imperative mode.

> Imperative mood just means "spoken or written as if giving a command or instruction". A few examples:
>
> 1.  Clean your room
> 1.  Close the door
> 1.  Take out the trash
>
> The imperative can sound a little rude; that's why we don't often use it. But it's perfect for Git commit subject lines.

## Body

1. just as in use imperative, present tense: “change” not “changed” nor “changes”
1. includes motivation for the change and contrasts with previous behavior

## Footer

### Breaking changes

All breaking changes have to be mentioned in footer with the description of the change, justification and migration notes.

Example,

```text
feat(home): write about me in markdown, reST or asciidoc

BREAKING CHANGE: Previously LANDING_PAGE_ABOUT was a dictionary that contained html tags. We used it
to create landing page. But users have demanded from the very beginning to be able to write the
landing page in markdown. This patch adds this feature. But in order to use it, you have to update
your configuration.

Closes #85
```

### Referencing issues

Closed bugs should be listed on a separate line in the footer prefixed with "Closes" keyword like this:

```text
Closes #234
```

or in case of multiple issues:

```text
Closes #123, #245, #992
```

In case your commit affects an issue, use "Updates" keyword

```text
Updates #234
```

## Examples

Following are few example commits that shows how Elegant has uses these guidelines.

### New Features

```text
feat(monetization): add BestAzon support
feat(Chinese): add better font support for Chinese language
feat(footer): make external links Nofollow
```

### Fixes

```text
fix(reST): indents in line blocks is not preserved
fix(gist): embedded Github gist are not laid out correctly
```

### Documentation

```text
docs(add): metadata variables
docs(add): release notes for 3.0.0
docs(update): change category of reading-time article
docs(update): set author information
```

### Miscellaneous

```text
chore(livereload): use es2015 syntax for gulp configuration
ci(docs): use sitemap plugin in production only
ci(docs): add default tasks.py file
refactor: move Google and Bing claims to their individual files
```

## Examples of Incorrect Commit Messages

This commit message starts with a capital letter and ends with a period

```text
doc(changes): Rewrite of multi-part plugin per issue 308.
```

This commit message does not use imperative mode.

```text
docs(change): updating status doc to reflect current state
```
