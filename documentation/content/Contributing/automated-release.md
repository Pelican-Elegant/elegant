---
Title: Fully automated version management and publishing
Date: 2019-07-20 23:17
Slug: fully-automated-version-management-and-publishing
Category: Contributing
Authors: Talha Mansoor
---

Elegant follows "realease early, realease often" software development philosophy. In this regard, our release process is fully automated.

We use [semantic-release](https://github.com/semantic-release/semantic-release) for version management and publishing.

Our semantic release configuration can be viewed [here](https://github.com/Pelican-Elegant/elegant/blob/master/.releaserc.json).

## CHANGELOG

It generates the change log automatically, therefore you do not have to update the [CHANGELOG](https://github.com/Pelican-Elegant/elegant/blob/master/CHANGELOG.md).

## New Releases and Version Number

semantic-release uses the commit messages to determine the type of changes in the codebase. Following [formalized conventions for commit messages]({filename}./git-commit-guidelines.md), semantic-release automatically determines the next semantic version number, generates a changelog and publishes the release.

Here is an example of the release type that will be done based on a commit messages:

| Commit message                                                                                                                                                                             | Release type           |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------- |
| fix(pencil): stop graphite breaking when too much pressure applied                                                                                                                         | Patch Release          |
| feat(pencil): add 'graphiteWidth' option                                                                                                                                                   | Minor Feature Release  |
| perf(pencil): remove graphiteWidth option<br><br>BREAKING CHANGE: The graphiteWidth option has been removed.<br>The default graphite width of 10mm is always used for performance reasons. | Major Breaking Release |

## Test Release Process Locally

To test semantic-release locally,

1. Install yarn
1. Run `yarn semantic-release`

It will run the all the checks and steps in dry run mode.
