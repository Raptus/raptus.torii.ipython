Introduction
============

This package extend raptus.torii with the functionality with ipython.

Use it with buildout:

[torii]
recipe = raptus.recipe.torii
socket-path = ${buildout:directory}/var/torii.sock
threaded = True
extends =
    raptus.torii.ipython



