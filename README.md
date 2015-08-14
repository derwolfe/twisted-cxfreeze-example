# Twisted example using cx-freeze

The code in this repository shows an example of using  [cx_freeze](https://bitbucket.org/anthony_tuininga/cx_freeze) with [Twisted](https://twistedmatrix.com/trac/).

The code adds a build step that generates an ```__init__.py``` at the path where the ```zope``` package lives.
The effect is that this alters a namespace package to a semi-normal package.

## How to run it

1. make a new ```virtualenv``` and activate it. I used python2.7 for this
2. run ```pip install -r requirements.txt```
3. run ```python setup.py bdist_dmg``` to build a mac application, or ```python setup.py bdist_msi``` for windows. The [cx-freeze docs](http://cx-freeze.readthedocs.org/en/latest/distutils.html) detail other options.
4. If on OS-X, open the dmg, then double click the application. This will start an echo server on localhost port 8000.
5. open a terminal and type "telnet localhost 8000"
6. If application has built, you should be able to connect and receive what you sent echoed back.

## Problems
This requires changing a dependency at build time. Namespace packages _should_ be able to function without this alteration.
