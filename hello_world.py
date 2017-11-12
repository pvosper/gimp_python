#!/usr/bin/env python


from gimpfu import gimp, register, main

"""doc string"""


def plugin_hello():
    gimp.message("Hello, GIMP world!\n")


register(
    "plugin_hello",         # proc_name called from cmd line
    "blurb",                # info about plug-in
    "help message",         # help
    "author",               # author
    "copyright",            # copyright holder for the plug-in
    "year",                 # copyright date
    "Hello World",          # label that the plug-in uses in the menu
    "*",                    # image types ie, RGB*, GRAY* &etc
    [],                     # method parameters (type, name, description, default [, extra]).
    [],                     # method results
    plugin_hello,           # name of method that will be called
    menu="<Image>/Local")   # location in menu bar

main()
