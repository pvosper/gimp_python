#!/usr/bin/env python

"""Image scaling for display on presonal web site
    1280 - Enlarge
    640 - Page
    320 - Index
    180 - Thumbnail
    Each should be derived from original (not chained)"""

from gimpfu import *


def web_toolbox(image, drawable, maximum_dimension, path, filename):

    if image.width > image.height:
        scale = float(maximum_dimension) / image.width
    else:
        scale = float(maximum_dimension) / image.height

    pdb.gimp_context_set_interpolation(3)
    pdb.gimp_image_scale(image, image.width*scale, image.height*scale)
    pdb.plug_in_unsharp_mask(image, drawable, 5.0, 0.5, 0)

    pdb.file_png_save(image, drawable, '/Users/paulvosper/temp/temp.png', 'temp.png', 0, 9, 1, 1, 1, 1, 1)

    return


register(
    "web_toolbox",                          # proc_name called from command line
    "Creates PNG files at standard dimensions", # info about plug-in
    "Scales image within specified maximum bounds while maintaining original aspect ratio",                         # help
    "Paul Vosper",                          # author
    "Paul Vosper",                          # copyright holder for the plug-in
    "2017",                                 # copyright date
    "Web Toolbox",                          # label that the plug-in uses in the menu
    "*",                                    # image types ie: RGB*, GRAY* &etc
    [
        (PF_IMAGE, "image", "Input image", None),
        (PF_DRAWABLE, "drawable", "Input layer", None),
        (PF_INT, "maximum_dimension", "Max?", 320),
        (PF_STRING, "path", "Path", "A Path"),
        (PF_STRING, "filename", "Filename", "A File Name"),
    ],                                      # method parameters
    [],                                     # method results
    web_toolbox,                            # name of method that will be called
    menu="<Image>/Local")                   # location in menu bar

main()
