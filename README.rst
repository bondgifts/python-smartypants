
python-smartypants
==================

SmartyPants is a tool for converting plain ASCII punctuation characters into
"smart" HTML entities, such as "straight" quotes into "curly" quotes and
"---" into em-dashes.

This forks extends that, allowing for plaing ASCII to be converted into "smart"
unicode encodings.


Installation
------------

Install the latest stable release, like so:

    pip install https://github.com/bondgifts/python-smartypants/archive/master.zip

or equivalently (with less keystrokes):

    pip install http://git.io/bond-smartypants


Usage Examples
--------------

Convert a plain ASCII string to a "smart" unicode encoded string:

.. code-block:: python

    import smartypants

    text = """There once was a man from Nantucket and he said 
    "What've you done with my bucket?"

    I replied, "it's a pail!"

    What a story...
    """

    smart_text = smartypants.smartyPants(text, unicode=True)
    # u'There once was a man from Nantucket and he said \n\u201cWhat\u2019ve you done with my bucket?\u201d\n\nI replied, \u201cit\u2019s a pail!\u201d\n\nWhat a story\u2026\n'

    print smart_text

You should get the following output:

    There once was a man from Nantucket and he said
    “What’ve you done with my bucket?”

    I replied, “it’s a pail!”

    What a story...


Check out the source for more information and options.


A Short History
---------------

SmartyPants was originally written in Perl by John Gruber. See
http://daringfireball.net/projects/smartypants/.

Chad Miller then ported it to Python 
(http://web.chad.org/projects/smartypants.py/), and Hao Lian packaged it and
put it on PyPI (http://pypi.python.org/pypi/smartypants).

Following that Jeff Schenck <http://jeffschenck.com/> added it to Github and 
made a small tweak where ``<tt>`` tags are skipped.

Bond needed this functionality but with support for unicode, so another fork was made.

And now, we are here.

