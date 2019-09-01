---
Title: Using 'yaspeller' with Elegant
Subtitle:
Slug: yaspeller-for-elegant
Category: Contributing
Tags:
Date: 2019-08-04 23:17
Summary: Elegant use the 'yaspeller' tool to scan for spelling mistakes.  This article gives more information about the tool and how to run it locally.
Keywords:
Authors: Jack De Winter
---

[TOC]

Even with most code editors having a spell checker installed and active by default, there is a
need to have the Elegant builds verify spelling against a known dictionary. The spell check
tool that was decided on by the team is the
[yaspeller tool](https://github.com/hcodes/yaspeller).

This tool is useful in that it has a number of options for altering what it considers eligible
for scanning. In its default mode, the `yaspeller` tool will scan everything in a Markdown
document except for text encapsulated within code blocks, such as:

````text
```text
[text ommitted for breverity]
```

OR

this `yaspeller` tool is cool

````

While `yaspeller` is a useful tool, it is not foolproof. When scanning the documentation
files, it often requires a bit of assistance in determining how to properly handle words which
do not appear in the standard dictionary.

## What To Do With Spelling Mistakes?

There are typically 4 categories of spelling mistakes: an honest mistake, a word to be added
to the project dictionary, a single situational misspelling, and intentional misspellings
within a block of text.

The way to address mistakes in the first category is simple. Fix them. If you are not 100%
sure that the word is spelled properly, consider using
[dictionary.com](https://www.dictionary.com/) to verify the spelling. If you search for a
given word and a simpler form of that word appears, scroll down to the related words section
and see if it is there.

## Adding A Word to the Project Dictionary

If the spelling mistake has been verified to be a properly spelled word, then the word jumps
over to the second category: a word to be added to the project dictionary. The root directory
of the project contains
[the project dictionary](https://github.com/Pelican-Elegant/elegant/blob/master/.yaspeller.json)
with a list of words that `yaspeller` should consider acceptable. Words added to the
dictionary in lower case will match upper case and lower case versions of the word, while words
added with any capitalization will force `yaspeller` to perform a case-sensitive match.

## A Single Intentional Misspellings within a Line of Text

For the third category, a single situational misspelling, the best example is included in the
article [Git Commit Guidelines]({filename}./git-commit-guidelines.md).
In that article, there is [a section]({filename}./git-commit-guidelines.md#type) describing the
legal values that can be associated with a commit type. While most of the values are fine,
there is one value that is the short form for "performance":

```text
- **perf**: A code change that improves performance <!-- yaspeller ignore -->
```

As this is the only word in the article that is intentionally spelled the way it is, the
line ends with the `<!-- yaspeller ignore -->` suffix to tell the `yaspeller` tool to ignore
the entire line. While we could add that single word to the project dictionary, it is more
clear to ignore the word for this given situation instead of adding it to the dictionary.

## Intentional Misspellings within a Block of Text

The final category, intentional misspellings within a block of text, is an extension of the
previous category, but dealing with multiple intentional misspellings, instead of a single
one. A good example of that would be specifying the contents for a table to show an example
to the user, such as the following:

<!-- yaspeller ignore:start -->

| Key | Value | File Name                    |
| --- | ----- | ---------------------------- |
| abc | 1     | stat-counter.md              |
| def | 2     | favicons-speed-dial-icons.md |

<!-- yaspeller ignore:end -->

If you look at the [Markdown for this article]({static}/Contributing/ya-spell-check.md),
notice how the table is surrounded with two HTML comments:
`<!-- yaspeller ignore:start -->` and `<!-- yaspeller ignore:end -->` with blank lines between
the comments and the block they are there to ignore.

With those comments in place, the `yaspeller` tool does not raise any issues with the Markdown
that generates this file, as it has been told to ignore everything starting with the first
comment and ending with the second comment. If these are removed, the `yaspeller` tool will
output the following errors:

```text
[ERR] /enlistments/elegant/documentation/content/Contributing/ya-spell-check.md 3450 ms
-----
Typos: 2
1. def (129:3)
2. favicons (129:13)

Capitalization: 1
1. abc (128:3, suggest: ABC)
-----
```

## Why Spell Check Locally?

Similar to the other checks that are performed on every submission, a spell check failure will
cause the build to fail.

Addressing any failures reported locally by this tool results in a smaller turn around time in
getting any spelling mistakes addressed. This in turn will save time when submitting changes
in a Pull Request, as you have already dealt with any errors that this tool may report.

### Prerequisites For Local Installation

Either [Node.js](https://nodejs.org/en/download/) or
[Yarn](https://yarnpkg.com/en/docs/install) must be installed on your system.

### How Do I Install It Locally?

You can install the `yaspeller` package using either NPM (Node.js) or Yarn as follows:

```bash
npm install -g yaspeller
```

OR

```bash
yarn global add yaspeller
```

### How Do I Use It Locally?

To invoke the `yaspeller` package for the documentation files for the Elegant project, go to
the root directory of your local repository and enter the following command:

```bash
yaspeller --only-errors documentation/content/ *.md
```

When executed, the `yaspeller` tool will recursively scan all of the `*.md` files under the
`documentation/content/` directory from the root of your local repository. The `--only-errors`
flags merely restricts any of the output to any errors that occur, instead of an ongoing stream
of what files it is scanning. As omitting the `--only-errors` flag only affects the output
and not the detection of spelling mistakes, feel free to not use it when running locally.
