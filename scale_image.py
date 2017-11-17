#!/usr/bin/env python

from gimpfu import *


def scale_image(image, max):

    if image.width > image.height:
        scale = float(max) / image.width
    else:
        scale = float(max) / image.height

    pdb.gimp_context_set_interpolation(3)    # INTERPOLATION-LANCZOS (3)
    pdb.gimp_image_scale(image, image.width*scale, image.height*scale)
    # pdb.plug_in_unsharp_mask(1, image, 5.0, 0.5, 0.0)   #TypeError: wrong parameter type
    #run-mode, image (unused), drawable, radius (in pixels), amount (strength of effect), threshold

    gimp.message("Interpolation: " + str(pdb.gimp_context_get_interpolation()) + "\n")

    return


register(
    "scale_image",                          # proc_name called from command line
    "Scale image within max bounds",        # info about plug-in
    "Scales image within specified maximum bounds while maintaining original aspect ratio",                         # help
    "Paul Vosper",                          # author
    "Paul Vosper",                          # copyright holder for the plug-in
    "2017",                                 # copyright date
    "Scale Image",                          # label that the plug-in uses in the menu
    "*",                                    # image types ie: RGB*, GRAY* &etc
    [
        (PF_IMAGE, "image", "Input image", None),
        (PF_INT, "max", "Max?", 320)
    ],                                      # method parameters
    [],                                     # method results
    scale_image,                            # name of method that will be called
    menu="<Image>/Local")                   # location in menu bar

main()
