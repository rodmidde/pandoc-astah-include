Include Astah images in Markdown with Pandoc
============================================
Include Macro to insert Astah Diagrams into a Markdown document using Pandoc.

Example
-------
``` {.astah file="designs/Sample.asta" caption="This is the caption" index=1 format="png"}
```

All parameters are required:
* file:     name of the asta file name
* caption:  caption to put under the image
* index:    normally a astah-file contains more than one diagram, use the index to point to the n-th diagram in the file
* format:   png or svg

Usage
-----
pandoc --filter astah.py astah-sample.md -o astah.pdf

Install
-------
Assuming you have [pandoc](http://pandoc.org/) and [python
2](https://www.python.org/) installed, I suggest you the following
options:

-   Copy `astah.py` and the astah-folder with the astah JARs to the directory where your markdown
    files are. Make `astah.py` executable.

Additionally the Python code makes use of
[`pandocfilters`](http://pandoc.org/scripting.html#but-i-dont-want-to-learn-haskell)
which can be installed as `pip install pandocfilters`.
