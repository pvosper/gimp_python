#!/usr/bin/env python

from gimpfu import *


def test_func():
    return

register(
    "test_func",            # proc_name called from command line
    "blurb",                # info about plug-in
    "help message",         # help
    "author",               # author
    "copyright",            # copyright holder for the plug-in
    "year",                 # copyright date
    "Test",                 # label that the plug-in uses in the menu
    "*",                    # image types ie: RGB*, GRAY* &etc
    [
    ],                      # method parameters
    [],                     # method results
    test_func,              # name of method that will be called
    menu="<Image>/Local")   # location in menu bar

main()
