# encoding: utf-8

from thunkapi import Thunk

__author__ = "Daniel Schauenberg"
__version__ = "0.1.0"
__license__ = "MIT"

def check(uid):
    """ shortcut function for checking thunks"""
    return Thunk().check(uid)

def create(name=None):
    """ shortcut function for creating thunks """
    return Thunk().create(name)

def poke(uid, state, payload=None):
    """shortcut function for poking thunks"""
    return Thunk().poke(uid, state, payload)
