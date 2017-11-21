#!/usr/bin/env python

"""Image scaling for display on presonal web site
    1280 - Enlarge
    640 - Page
    320 - Index
    180 - Thumbnail
    Each should be derived from original (not chained)"""

from gimpfu import *


def web_toolbox(image, drawable, maximum_dimension, path, filename):

    # Create working image for destructive manipulation
    working_image = pdb.gimp_image_duplicate(image)
    working_layer = pdb.gimp_image_merge_visible_layers(working_image, CLIP_TO_IMAGE)

    # Create scale factor to fit working image
    # todo rectangular limits as option, rather than square
    if working_image.width > working_image.height:
        scale = float(maximum_dimension) / working_image.width
    else:
        scale = float(maximum_dimension) / working_image.height

    # Scale and adjust working image
    pdb.gimp_context_set_interpolation(3)
    pdb.gimp_image_scale(working_image, working_image.width*scale, working_image.height*scale)
    pdb.plug_in_unsharp_mask(working_image, working_layer, 5.0, 0.5, 0)

    # Export working image as PNG
    pdb.file_png_save(working_image, working_layer, '/Users/paulvosper/temp/temp.png', 'temp.png', 0, 9, 1, 1, 1, 1, 1)

    pdb.gimp_image_delete(working_image)

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
