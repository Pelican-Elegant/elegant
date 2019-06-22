# Where do I start?

Developing Elegant is a community effort, so you are very welcome to help develop it further into the most elegant theme out there.

The main repository of Elegant is on [GitHub][elegant], which you may fork and then submit pull requests to, in order for them to be merged.

If you found any issues, or have ideas how to improve the theme, please submit an [issue].

Also see issues tagged as [Pull Request Welcome](https://github.com/Pelican-Elegant/elegant/labels/pull%20request%20welcome) – these are issues that are not directly on our roadmap, but if you have time to contribute, we would be very glad to review and accept your pull request.

If you want to contribute to documentation instead, do so in the [documentation repository][documentation]. Some easy tasks to tackle there are tagged as [Good First Issue](https://github.com/Pelican-Elegant/documentation/labels/good%20first%20issue)

# Contributing Code

1. Create a new git branch specific to your changes, instead of making your commits in the master branch. For example, create a branch `fix-issue-119` and add commits to it that fix “issue 119”.
2. Update the [CHANGELOG]
3. Create pull request from your fix branch, say `fix-issue-119`, against `next` branch of Elegant. (We use `master` branch to make new releases. `next` is used for development.)
4. Each pull request should only have a single feature or fix. Do not add multiple features or bug fixes to the same pull request.
5. Squash your commits to reduce noise from commit history. Use your better judgement to decide which commits should stay in the commit history, or consult project maintainers if confused.
6. Have (at least) one other active contributor review your code.
7. Once at least one code reviewer has approved it, it will can be merged.

## Git Tips for Newcomers

Here are some tips on how to make your life with Git easier when contributing.

### How To Set Up Your Git

1. Create a fork of the [Elegant repository][elegant] by clicking on the “Fork” button.
2. Clone your fork to your computer by clicking on the “Clone or download” button and following the instructions there.
3. When in the Git repository of your fork, run the following command to set the main repository as the upstream: `git remote add upstream https://github.com/Pelican-Elegant/pelican-elegant.git`

### Updating/Rebasing to Upstream

Occasionally – often before a pull request is able to be merged – you will need to update your own (fork) repository to the upstream (i.e. [Elegant][elegant]) development (i.e. `next`) branch. This can be done as follows:

1. `git fetch upstream next`
2. `git rebase upstream/next`

### Squash Commits & More Complex Rebasing

When creating a pull request in GitHub, you have the option to squash all commits, but sometimes you need to fix either the mess you made or some clashes that prevent a merge of the two branches.

In both cases, the following command is your swiss-army knife:

`git rebase --interactive upstream/master`

For more on the interactive rebase command of Git, see [its official documentation][git_rebase].

[git_rebase]: https://git-scm.com/docs/user-manual#interactive-rebase

# New Features and Styles

If you plan to add new features to the theme, please make sure that:

- you set sensible defaults so the theme works out of the box, without forcing the user to set any variable
- your changes do not negatively effect readability and reading experience
- your changes do not cause distraction for the reader
- any bigger features should go through the voting process (see below)

# Code style

Please make sure to follow the code style of the existing codebase.

Specifically:

## Code/Template Formatting Rules

- use single (`''`) rather than double (`""`) quotation marks for Jinja strings
- in Jinja print statements, surround the variable with spaces inside curly braces – for example: `{{ foo.bar }}`
- use double (`""`) quotation marks around HTML attributes
- end files with a newline

## CSS Formatting Rules

- font name’s first letter should be capital
- add a space after comma
- declarations should be sorted alphabetically
- use a single space between the last selector and the opening brace that begins the declaration block
- group together related classes and identities
- add a space after colon
- remove leading 0s
- remove unit specification after 0 values
- use three-digit Hex notation for colors whereever possible
- use hyphen `-` instead of underscore `_` in class and identity names

Refer to [Google's HTML/CSS Style Guide][google_style_guide] for all other formatting rules.

# Voting Process

Any new features, bigger changes, decisions on what should constitute the next milestone or wider goals etc. should go through a vote, as follows.

1. Open a new issue to describe it and to kick-start a discussion.
1. As soon as a suggestion (or several) are set in place, set a deadline, no shorter than 10 days. Also at this stage tag the issue with the “vote” label.
1. People can vote with the :+1: and :-1: emoji on individual suggestions. Anyone may cast votes for as many suggestions as they want.
1. At the end of the deadline, the suggestion with most votes (= № of :+1: - № of :-1:) is taken.

# Licensing (Inbound=Outbound)

All contributions will be understood to be made under the same (inbound) license as the main (outbound) license of the repository it is being contributed to – so [MIT License][] for all [code/theme][elegant] contributions, and [CC-BY-SA-3.0][] for all [documentation][] contributions.

If you are contributing code that is not yours, make sure to indicate where you got the code from (and who the author/copyright holder is) and what license you got it under.

[cc-by-sa-3.0]: https://spdx.org/licenses/CC-BY-SA-3.0.html
[changelog]: https://github.com/Pelican-Elegant/elegant/blob/master/CHANGELOG.md
[contributing]: ./CONTRIBUTING.md
[documentation]: https://github.com/Pelican-Elegant/documentation
[elegant]: https://github.com/Pelican-Elegant/elegant
[google_style_guide]: https://google.github.io/styleguide/htmlcssguide.html
[issue]: https://github.com/Pelican-Elegant/elegant/issues/
[mit license]: https://spdx.org/licenses/MIT.html
