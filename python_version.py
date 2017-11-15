#!/usr/bin/env python


from gimpfu import *

"""Testing which version of Python gets run inside Gimp"""


def python_version():
    import platform
    version = "Python Version: " + platform.python_version() + "\n"
    gimp.message(version)


register(
    "python_version",       # proc_name called from cmd line
    "blurb",                # info about plug-in
    "help message",         # help
    "author",               # author
    "copyright",            # copyright holder for the plug-in
    "year",                 # copyright date
    "Python Version",       # label that the plug-in uses in the menu
    "*",                    # image types ie, RGB*, GRAY* &etc
    [],                     # method parameters (type, name, description, default [, extra]).
    [],                     # method results
    python_version,         # name of method that will be called
    menu="<Image>/Local")   # location in menu bar

main()
