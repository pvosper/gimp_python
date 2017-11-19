#!/usr/bin/env python


"""Display current working directory for debugging"""


from gimpfu import *
import os

def display_cwd():

    current_working_directory = "Current Working Directory: " + os.getcwd() + "\n"
    gimp.message(current_working_directory)


register(
    "display_cwd",          # proc_name called from cmd line
    "blurb",                # info about plug-in
    "help message",         # help
    "author",               # author
    "copyright",            # copyright holder for the plug-in
    "year",                 # copyright date
    "Current Working Directory",       # label that the plug-in uses in the menu
    "*",                    # image types ie, RGB*, GRAY* &etc
    [],                     # method parameters (type, name, description, default [, extra]).
    [],                     # method results
    display_cwd,            # name of method that will be called
    menu="<Image>/Local")   # location in menu bar

main()
