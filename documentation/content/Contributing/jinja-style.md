---
Title: Code Style for Jinja2
Date: 2019-07-03 22:17
Slug: code-style-for-jinja2
Category: Contributing
authors: Talha Mansoor
---

Please make sure to follow the code style of the existing code base.

Specifically:

- use single (`''`) rather than double (`""`) quotation marks for Jinja strings
- in Jinja print statements, surround the variable with spaces inside curly braces – for example: `{{ foo.bar }}`
- use double (`""`) quotation marks around HTML attributes
- end files with a newline
