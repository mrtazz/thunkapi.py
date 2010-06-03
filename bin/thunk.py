#!/usr/bin/env python
# encoding: utf-8

""" executable to interact with thunk.us using the thunk.py library """

import thunkapi
from optparse import OptionParser


def init_parser():
    """ function to init option parser """
    usage = "usage: %prog [-x action] [-p payload] [-n name] [-s state] UID"

    parser = OptionParser(usage, version="%prog "+thunkapi.__version__)
    parser.add_option("-x", "--action", action="store", dest="action",
                      help="action to execute")
    parser.add_option("-p", "--payload", action="store", dest="payload",
                      help="payload for the thunk")
    parser.add_option("-n", "--name", action="store", dest="name",
                      help="name of the thunk")
    parser.add_option("-s", "--state", action="store", dest="state",
                      help="state of the thunk to poke")

    (options, args) = parser.parse_args()
    return (parser, options, args)

def main():
    """ main function """
    # get options and arguments
    (parser, options, args) = init_parser()

    if len(args) < 1:
        parser.error("No UID given.")

    if options.action:
        action = options.action
        if action == "poke":
            if not options.state:
                parser.error("No poke state given.")
            else:
                ret = thunkapi.poke(args[0], options.state, options.payload)
        elif action == "create":
            ret = thunkapi.create(options.name)
        else:
            ret = thunkapi.check(args[0].split(","))

    else:
        ret = thunkapi.check(args[0].split(","))

    try:
        thunks = ret["thunks"]
    except KeyError:
        thunks = [ret]

    print "Thunks:"
    for thnk in thunks:
        print "==="
        for key in thnk.keys():
            print "%s: %s" % (key, thnk[key])

if __name__ == '__main__':
    main()
