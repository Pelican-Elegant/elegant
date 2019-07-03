---
Title: Git Tips for Beginners
Date: 2019-07-03 21:57
Slug: git-tips-for-beginners
Category: Contributing
---

Here are some tips on how to make your life with Git easier when contributing.

## How To Set Up Your Git

1. Create a fork of the [Elegant repository][elegant] by clicking on the “Fork” button.
2. Clone your fork to your computer by clicking on the “Clone or download” button and following the instructions there.
3. When in the Git repository of your fork, run the following command to set the main repository as the upstream: `git remote add upstream https://github.com/Pelican-Elegant/pelican-elegant.git`

## Updating/Rebasing to Upstream

Occasionally – often before a pull request is able to be merged – you will need to update your own (fork) repository to the upstream (i.e. [Elegant][elegant]) development (i.e. `next`) branch. This can be done as follows:

1. `git fetch upstream next`
2. `git rebase upstream/next`

## Squash Commits & More Complex Rebasing

When creating a pull request in GitHub, you have the option to squash all commits, but sometimes you need to fix either the mess you made or some clashes that prevent a merge of the two branches.

In both cases, the following command is your Swiss-army knife:

`git rebase --interactive upstream/master`

For more on the interactive rebase command of Git, see [its official documentation][git_rebase].

[git_rebase]: https://git-scm.com/docs/user-manual#interactive-rebase
[elegant]: https://github.com/Pelican-Elegant/elegant
