============
thunkapi.py
============

Introduction
=============
thunkapi.py is a python library and command line client for
interacting with the thunk.us_ web service.

Installation
=============
Install via pip::

    pip install thunkapi

Or if you must::

    easy_install thunkapi


Usage
======
thunk.py can be imported into any python module::

    import thunkapi

    thunkapi.create()
    thunkapi.poke(UID, state, payload)
    thunkapi.check(uid)

There is also a command line client to use::

    thunk.py UID
    thunk.py -x check UID
    thunk.py -x check "UID1,UID2,UID3"
    thunk.py -x poke -s state -p payload UID
    thunk.py -x create

.. _thunk.us: http://thunk.us
