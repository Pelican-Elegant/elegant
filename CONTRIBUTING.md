# Where do I start?

Developing Elegant is a community effort, so you are very welcome to help develop it further into the most elegant theme out there.

The main repository of Elegant is on [GitHub][elegant], which you may fork and then submit pull requests to, in order for them to be merged.

If you found any issues, or have ideas how to improve the theme, please submit an [issue][].

Also see issues tagged as [Pull Request Welcome](https://github.com/Pelican-Elegant/elegant/labels/pull%20request%20welcome) – these are issues that are not directly on our roadmap, but if you have time to contribute, we would be very glad to review and accept your pull request.

# Contributing Code

1. Create a new git branch specific to your changes, instead of making your commits in the master branch. For example, create a branch `fix-issue-119` and add commits to it that fix "issue 119".
1. Create pull request from that branch.
1. Each pull request should only have a single feature or fix. Do not add multiple features or bug fixes to the same pull request.
1. Squash your commits to reduce noise from commit history. Use your better judgement to decide which commits should stay in the commit history, or consult project maintainers if confused.

3. Create pull request against the `next` branch. We use `master` branch to
make new releases. `next` is used for development.

# New Features and Styles

If you plan to add new features to the theme, please make sure that:

1. you set sensible defaults so the theme works out of the box, without forcing the user to set any variable
1. your changes do not negatively effect readability and reading experience
1. your changes do not cause distraction for the reader

# Code style

Please make sure to follow the code style of the existing codebase.

Specifically:

## Code/Template Formatting Rules

1. use single (`''`) rather than double (`""`) quotation marks for Jinja strings
1. in Jinja print statements, surround the variable with spaces inside curly braces – for example: `{{ foo.bar }}`
1. use double (`""`) quotation marks around HTML attributes
1. end files with a newline

## CSS Formatting Rules

1. font name's first letter should be capital
1. add a space after comma
1. declarations should be sorted alphabetically
1. use a single space between the last selector and the opening brace that begins the declaration block
1. group together related classes and identities
1. add a space after colon
1. remove leading 0s
1. remove unit specification after 0 values
1. use three-digit Hex notation for colors whereever possible
1. use hyphen `-` instead of underscore `_` in class and identity names

Refer to [Google's HTML/CSS Style Guide][google_style_guide] for all other formatting rules.

# Licensing (Inbound=Outbound)

All contributions will be understood to be made under the same (inbound) license as the main (outbound) license of the repository it is being contributed to – so [MIT License][] for all [code/theme][elegant] contributions, and [CC-BY-SA-3.0][] for all [documentation][] contributions.

If you are contributing code that is not yours, make sure to indicate where you got the code from (and who the author/copyright holder is) and what license you got it under.


[elegant]: https://github.com/Pelican-Elegant/elegant
[documentation]: https://github.com/Pelican-Elegant/documentation
[issue]: https://github.com/Pelican-Elegant/elegant/issues/
[contributing]: ./CONTRIBUTING.md
[google_style_guide]: https://google.github.io/styleguide/htmlcssguide.html
[MIT License]: https://spdx.org/licenses/MIT.html
[CC-BY-SA-3.0]: https://spdx.org/licenses/CC-BY-SA-3.0.html
