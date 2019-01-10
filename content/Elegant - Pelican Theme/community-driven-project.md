---
Title: Elegant grows into a community-led project
Tags: pelican-theme, web-design, project-management
Category: Announcements
Date: 2019-01-05 19:40
Slug: community-led-project
Subtitle: The beggining of a beautiful friendship
Summary:  Elegant has grown into a community-driven project. It also got a new website and organisational structure, culminating in its biggest release yet.
Keywords:
---
[TOC]


# Move to community development model

Elegant was started in 2012 by [Talha Mansoor][talha131] as a theme for the [Pelican][] static site generator. In quite a short time it grew in popularity due to its clean and functional style.

In November 2018, Elegant’s wider community was called into a [discussion about the future of their beloved theme][future]. The call-out and initial organisation was made by [Matija Šuklje][silverhook], with many responding – and with Talha as the first to support the proposal of changing the development model from a single-developer to a community-led project. The same month several pillars for a community-led project were established.

[Talha Mansoor][talha131] moved Elegant from a simple personal repository to a separate organisation (more on that below), which currently consist of (in alphabetical order):

- [Pablo Iranzo Gómez – “iranzo”][iranzo] – owner
- [Talha Mansoor – “talha131”][talha131] – owner
- [Ashwin Vishnu Mohanan – “ashwinvis”][ashwinvis] – member
- [Matija Šuklje – “silverhook”][silverhook] – owner
- [Andrew Wegner – “AWegnerGitHub”][AWegnerGitHub] – member
- [Calf Zhou – “calfzhou”][calfzhou] – owner

This way, the bus factor of the project has greatly improved and we can look into a bright future of this wonderful theme!

[pelican]: https://getpelican.com
[AWegnerGitHub]: https://andrewwegner.com
[ashwinvis]: https://ashwinvis.github.io/
[calfzhou]: http://gocalf.com
[talha131]: http://oncrashreboot.com
[iranzo]: https://iranzo.github.io/
[silverhook]: https://matija.suklje.name
[future]: https://github.com/talha131/pelican-elegant/issues/173


# New governance model

Since the code base is suddenly tended by several people, some basic rules of governance had to be set up in order to avoid people stepping on each-others toes.

As a start, the above-listed project members are not set in stone and discussion just started on [guidelines for adding new members and admins to the organization][new_members].

We clarified the outbound and inbound licensing situation. Elegant is released (= outbound license) under the [MIT][] license and its documentation under the [CC-BY-4.0][] license. All code contributions are made directly under the “Inbound=Outbound licensing model”, as the license everyone contributes their code under (i.e. inbound license) is exactly the same as the license that the code is then being released under to the general public.

The [contribution guidelines][contributing] have been updated as well and should be easier to follow now.

We have also started discussing [how to vote on new features and other important decisions][vote], which should be implemented soon.

If you are interested in helping with the governance processes, feel free to check out the [issues relevant to project management][governance].

[governance]: https://github.com/Pelican-Elegant/elegant/labels/project%20management
[MIT]: https://spdx.org/licenses/MIT.html
[CC-BY-4.0]: https://creativecommons.org/licenses/by/4.0/
[new_members]: https://github.com/Pelican-Elegant/elegant/issues/193
[vote]: https://github.com/Pelican-Elegant/elegant/issues/180


# New website & documentation

Any good project needs good documentation and deserves a good homepage.

We decided to eat our own dogfood by having our documentation run on an Elegant-themed Pelican instance. This would double as a proper demo website as well as a common testing ground for the team.

Luckily for us, as Pelican is easy to migrate, [Talha][talha131] very quickly set up a [new repository][docs] with all that is needed to build Elegant’s documentation and homepage.

Together with Talha, [Pablo][iranzo] and [Ashwin][ashwinvis] were the most to be thanked for setting up a CI system that automatically generates Elegant’s new homepage and documentation on each commit.

… and so <https://pelican-elegant.github.io/> was born!


# Future releases

As we write this blog post, the discussion on [how to tackle future releases][future_releases] is still on-going, so it is a great time for you, dear (potential) Elegant user, to join in and influence our plans together.

Right now, the discussion seems to go in the line of:

1. [2.0][] – All those fixes and features that do not require creating Pelican plugins or changes in Pelican code. This release will have updated and additional documentation too. (what we [just released][release_2.0])
1. [2.1][] – Make theme compatible with Pelican 4.* Open PR against branch "dev-2.1".
1. [3.0][] – Next generation Elegant – the biggest goal is to remove dependency on Bootstrap, to make it easier to maintain. 3.0.0 should have feature parity with 2.0.0.

[release_2.0]: {filename}/v2.md
[2.0]: https://github.com/Pelican-Elegant/elegant/milestone/3
[2.1]: https://github.com/Pelican-Elegant/elegant/milestone/5
[3.0]: https://github.com/Pelican-Elegant/elegant/milestone/4
[future_releases]: https://github.com/Pelican-Elegant/elegant/issues/192


# Invitation to participate

If you have not tried Elegant yet do give it a try and even if you _have_ tried it before, please do not hesitate to give Elegant a new try – a lot has improved!

You can use the new release already, but if you just want to browse a bit – our brand new documentation and homepage at <https://pelican-elegant.github.io> is a great demo for the theme.

If you like the theme and would like to contribute to Elegant, you are most welcome to do so. Even though Pelican is written in Python, no coding skills are needed to help out with Elegant, as themes consist mostly of [Jinja][] templates, CSS and HTML. It is honestly very easiy to get into. If you want to help out, but have no idea where to start, we keep a list of [low-priority features that are just waiting for you to pick up][pr_welcome]. Please consult the [`CONTRIBUTING.md`][contributing] file for the technical details.

Another way to contribute is to help with the [website/documentation][docs]. We are keeping a list of [good first issues][docs_first] for newbies to get involved – these are easy to tackle, but in no way less helpful. With the migration from Talha’s personal website, while functional, there is still quite some work to make Elegant’s new home neat and tidy. So there are a lot of small tasks where you can help out here and make an impact!

And, of course, reporting bugs and filing feature requests to further improve Elegant (and its documentation), is also very much welcome.

[Jinja]: http://jinja.pocoo.org/
[contributing]: https://github.com/Pelican-Elegant/elegant/blob/master/CONTRIBUTING.md
[pr_welcome]: https://github.com/Pelican-Elegant/elegant/labels/pull%20request%20welcome
[docs]: https://github.com/Pelican-Elegant/documentation/
[docs_first]: https://github.com/Pelican-Elegant/documentation/labels/good%20first%20issue

*[CI]: Continuous Integration
*[CSS]: Cascading Style Sheets
*[HTML]: HyperText Markup Language
