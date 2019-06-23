Title: How to display Line Numbers in Code Snippets
Tags: markdown, reST, code-snippets, gist
Category: Appearance & Style
Date: 2013-11-05 17:36
Slug: how-to-display-line-numbers-in-code-snippets
Disqus_identifier: wmo972t-how-to-display-line-numbers-in-code-snippets
Subtitle:
Summary: reStructuredText and Markdown have directives that generate line numbers for code blocks. Use them to display line numbers in code snippets.
Keywords: codehilite, python-markdown

reStructuredText and Markdown have directives that generate line numbers for
code snippets. Install [Pygments](http://pygments.org/) to use these directives.

Following examples will generate this output,

    #!python
    def example():
        print 'Hello World'

## reStructuredText

reStructuredText has `code-block` directive to insert code snippets in your
markup. Use `linenos` flag to switch on line numbers for the snippet.

    :::reST
    .. code-block:: python
        :linenos:

        def example():
            print 'Hello World'

## Markdown

[Python-Markdown](https://github.com/waylan/Python-Markdown) uses
[CodeHilite](http://pythonhosted.org/Markdown/extensions/code_hilite.html)
extension for syntax highlighting. Setup CodeHilite, then use Shebang `!#` to
generate line numbers.

    :::markdown
    #!python
    def example():
        print 'Hello World'
