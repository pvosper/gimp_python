#!/usr/bin/env python

from gimpfu import *


# method must be registered
def scale_image(image, number):
    pdb.gimp_image_scale(image, image.width*number, image.height*number)
    return

register(
    "scale_image",                          # proc_name called from command line
    "Scales image within specified limit",  # info about plug-in
    "help message",                         # help
    "Paul Vosper",                          # author
    "Paul Vosper",                          # copyright holder for the plug-in
    "2017",                                 # copyright date
    "Scale Image",                          # label that the plug-in uses in the menu
    "*",                                    # image types ie: RGB*, GRAY* &etc
    [
        (PF_IMAGE, "image", "Input image", None),
        (PF_INT, "max", "Max?", 640)
    ],                                      # method parameters
    [],                                     # method results
    scale_image,                            # name of method that will be called
    menu="<Image>/Local")                   # location in menu bar

main()
