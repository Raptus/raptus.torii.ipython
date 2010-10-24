Introduction
============
Torii allow the access to a running zope server over a unix-domain-socket. Torii make
also possible to run scripts from the command line to the server. In addition it's provide a python-
prompt connected to the zope-server. It means the full access of the Zope and ZODB at the runtime.


A implementation of ipython. Code-completion, readline and colored python prompt.

Use it with buildout::

    [torii]
    recipe = raptus.recipe.torii
    socket-path = ${buildout:directory}/var/torii.sock
    threaded = True
    extends =
        raptus.torii.ipython

`more information at raptus.torii <http://pypi.python.org/pypi/raptus.torii>`_

Copyright and credits
=====================

raptus.torii is copyright 2010 by raptus_ , and is licensed under the GPL. 
See LICENSE.txt for details.

.. _raptus: http://www.raptus.ch/ 