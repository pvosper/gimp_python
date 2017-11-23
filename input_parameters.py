#!/usr/bin/env python


from gimpfu import *


def in_params(alpha, beta, gamma):
    message_string = "alpha: " + alpha + "\nbeta: " + beta + "\ngamma: " + gamma + "\n"
    gimp.message(message_string)

    return

register(
    "in_params",            # proc_name called from cmd line
    "blurb",                # info about plug-in
    "help message",         # help
    "author",               # author
    "copyright",            # copyright holder for the plug-in
    "year",                 # copyright date
    "Input Parameters",     # label that the plug-in uses in the menu
    "*",                    # image types ie, RGB*, GRAY* &etc
    [
        (PF_STRING, "one", "First String", "a b c d e"),
        (PF_STRING, "two", "Second String", "f g h i j"),
        (PF_STRING, "three", "Third String", "k l m n o"),
    ],                      # method parameters (type, name, description, default [, extra]).
    [],                     # method results
    in_params,              # name of method that will be called
    menu="<Image>/Local")   # location in menu bar

main()
