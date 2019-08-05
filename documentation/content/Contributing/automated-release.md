---
Title: Automated Version Management and Publishing
Subtitle:
Slug: fully-automated-version-management-and-publishing
Category: Contributing
Tags:
Date: 2019-07-20 23:17
Summary: Elegant utilizes a 'release early, release often' philosophy that embraces a fully automated release process.
Keywords:
Authors: Talha Mansoor, Jack De Winter
---

[TOC]

The Elegant project follows a "release early, release often" software development philosophy.
By employing this philosophy, we are able to have each team member working on a different
aspect of the project with little friction from each other's changes. At any point, any team
member can pull changes that have been made in another branch to their fork of the repository
and exercise their changes with complete confidence.

Another benefit of this philosophy if that in order to attain this goal, our release process
must be fully automated.

## Release Versions

Version management and publishing is accomplished using the
[semantic-release](https://github.com/semantic-release/semantic-release) tool and it's
[configuration file](https://github.com/Pelican-Elegant/elegant/blob/master/.releaserc.json).
This tool entirely removes any human intervention needed for determining how to label
the next release of the project.

## CHANGELOG File Updates

An integral part of the release is the generation of information to be added to the
[CHANGELOG file](https://github.com/Pelican-Elegant/elegant/blob/master/CHANGELOG.md).
By mandating that any commits for the project follow a
[mandated format for the commit messages]({filename}./git-commit-guidelines.md),
the commits being added to the release can have their commit messages scanned by a tool,
including relevant portions into the release notes. Similar to the previous paragraph on
version management, this can be accomplished without any need for human intervention.

### Example of an Automated Release

Here is an example of an automated release. This is the
[Version 3.2.0](https://github.com/Pelican-Elegant/elegant/releases/tag/V3.2.0) that
was released on 30-Jul-2019. The specifics about the release can be obtained by clicking
on the 7 digit hexadecimal number below the version tag on the left side of the page, which
will take you to the [release commit](https://github.com/Pelican-Elegant/elegant/commit/48f39643edd6c3b7449af5dae8ade6323bc7c21f).

![automated release]({static}/images/automated-release.png)

This release can also be viewed by performing a `git log --grep=chore(release)` command and
looking for the specific release information in the logs. You can then view the specific
information for that commit by using the `git show` command with the hash for the release's
commit, `git show 48f39643edd6c3b7449af5dae8ade6323bc7c21f`.

Using either process, the result will look like:

```text
commit 48f39643edd6c3b7449af5dae8ade6323bc7c21f
Author: semantic-release-bot <semantic-release-bot@martynus.net>
Date:   Tue Jul 30 19:56:10 2019 +0000

    chore(release): 3.2.0 [skip ci]

    # [3.2.0](https://github.com/Pelican-Elegant/elegant/compare/V3.1.0...V3.2.0) (2019-07-30)

    ### Bug Fixes

    * **freelists:** open FreeLists subscription form in a new tab ([f81657c](https://github.com/Pelican-Elegant/elegant/commit/f81657c))
    * **freelists:** replace deprecated subscription form with button ([9bfe3c1](https://github.com/Pelican-Elegant/elegant/commit/9bfe3c1)), closes [#412](https://github.com/Pelican-Elegant/elegant/issues/412)
    * **freelists:** rm unused include ([27f0831](https://github.com/Pelican-Elegant/elegant/commit/27f0831))

    ### Features

    * **comments:** reduce transition duration from 500 to 200 ([b86e13d](https://github.com/Pelican-Elegant/elegant/commit/b86e13d))
    * **favicon:** add 180x180 dimension shortcut icon support ([dd2ed24](https://github.com/Pelican-Elegant/elegant/commit/dd2ed24))
    * **filter:** add black list, white list feature for Disqus ([4887aec](https://github.com/Pelican-Elegant/elegant/commit/4887aec))
    * **filter:** add black list, white list feature for FreeLists ([2407cc8](https://github.com/Pelican-Elegant/elegant/commit/2407cc8))
    * **filter:** add black list, white list feature for Mailchimp ([b96122d](https://github.com/Pelican-Elegant/elegant/commit/b96122d))
```

In the main body of the output, there are links with associated text which are 7 digit
hexadecimal numbers. Each of these links is to a specific commit that was part of the
release. If you follow the link, you can verify that the correct text is being used for the
release notes.

Additionally, there are links that are associated with text that starts with an octothorpe
(`#` character, sometimes referred to as the hash, hash-tag, or pound character)
followed by an integer. Each of these links is to an issue that was either updated or
fixed by the given commit. As with the above paragraph, you can verify that the correct
issue was associated with the commit in the release notes by following the commit links and
looking for any issue number at the end of the commit text.
