---
Title: Use Commitizen for Git commits
Subtitle: Recommended
Date: 2019-07-22 14:15
Slug: use-commitizen-for-git-commits
Category: Contributing
Authors: Talha Mansoor
---

When you commit with [Commitizen](https://github.com/commitizen/cz-cli), you'll be prompted to fill out any required commit fields at commit time.

## Prerequisites

### Step 1: Install NodeJS and Yarn

Install [Node.js](https://nodejs.org/en/download/) and [Yarn](https://yarnpkg.com/en/docs/install) on your system.

If you are on Windows then try installing them with [scoop.sh](https://scoop.sh/). It saves time and makes update easier.

### Step 2: Install gulp

Run this command from your command line terminal.

```bash
yarn global add commitizen
```

## Use Commitizen

We have already gone through the trouble of making Elegant repository [Commitizen friendly](https://github.com/commitizen/cz-cli#making-your-repo-commitizen-friendly).

All you have to do is to stage your changes and then run

```bash
git-cz
```

It will prompt you for questions. Just answer them. Commitizen will automatically format it to conform to [Elegant Git commit guidelines]({filename}./git-commit-guidelines.md).

If your Git commit fails for some reasons, like due to [Git hooks]({filename}./pre-commit.md), then you can fix the issue and rerun Commitizen using,

```bash
git cz --retry
```

When you use `--retry`, Commitizen does not prompt for answers and reuse the answers that you last submitted.

## Video Demonstration

<script id="asciicast-258540" src="https://asciinema.org/a/258540.js" async></script>
