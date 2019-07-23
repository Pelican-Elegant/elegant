---
Title: Use Pre-Commit Git Hooks
Date: 2019-07-22 23:17
Slug: use-pre-commit-git-hooks
Category: Contributing
Authors: Talha Mansoor
---

Since Elegant has moved to [bazar development model]({filename}./community-driven-project.md), we want to make sure all patches follow the same stylistic guidelines.

We leverage Git hooks to auto format all the patches. But Git hooks are hard to manage and sync. Therefore we decided to use [Pre-Commit](https://pre-commit.com/) which provides an abstraction over the Git hooks.

Pre-commit makes managing, sharing and updating the Git hooks very easy. You can set it up once and then forget about it.

To install pre-commit,

```bash
pip install pre-commit
```

Then in the root of your Elegant repository run,

```bash
pre-commit install
```

That's it. You don't have to worry about it anymore.

Next time when you will try to do a Git commit, pre-commit will download all the tools required for running the Git hooks. It may take sometime but this is a one time operation. Once tools are in the place, Git hooks will run before every Git commit.

In almost all cases, you will not have to do anything. It will run the hooks, format the files and notify you of error. You will then stage the changed files and retry your commit.

## Why use pre-commit at all?

Pre-commit runs Git hooks that among other things,

1. Run [Prettier](https://github.com/prettier/prettier) on Markdown, CSS, JS and json files
1. Run [Black](https://github.com/python/black) on Python files
1. Removes trailing whitespace

## Pull Requests and pre-commit

We have setup pre-commit to run on all pull requests using Travis CI. Travis runs pre-commit and on error, reports build failure.
