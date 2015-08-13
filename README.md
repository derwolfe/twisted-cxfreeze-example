# Twisted example using cx-freeze

The code in this repository is meant to show an example of using  [cx_freeze](https://bitbucket.org/anthony_tuininga/cx_freeze) with [Twisted](https://twistedmatrix.com/trac/).

The only real change, is that one of the build steps involves adding an ```__init.py``` file to the path where ```zope``` lives.
The effect is that this alters a namespace package to a semi-normal package.

## How to run it

1. make a new virtualenv and activate it. I used python2.7 for this
2. run ```pip install -r requirements.txt```
3. run ```python setup.py bdist_dmg``` to build a mac application, or ```python setup.py bdist_msi``` for windows. Other options can be found in the [cx-freeze docs](http://cx-freeze.readthedocs.org/en/latest/distutils.html).
4. If on OS-X, open the dmg, then double click the application. This will start an echoserver on localhost port 8000.
5. open a terminal and type "telnet localhost 8000"
6. If application has built correctly, you should be able to connect and receive what you sent echoed back.

## Problems
This requires changing a dependency at build time. It seems like namespace packages _should_ be able to function without this type of alteration.
