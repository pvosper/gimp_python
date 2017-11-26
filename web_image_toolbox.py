#!/usr/bin/env python

"""Image scaling for display on personal web site
    2048 - Zoom (_zoo)
    1024 - Display (_dis)
    512 - Index (_ind)
    Each should be derived from original (not chained)"""


from gimpfu import *
import os


# This can be used for method parameters
# todo: This is valid for OSX, but not cross-platform
home_dir = os.path.expanduser('~')


def web_toolbox(image, drawable, project, title, dir, zoo_w, zoo_h, dis_w, dis_h, ind_w, ind_h):

    export_sizes = [('zoo', zoo_w, zoo_h), ('dis', dis_w, dis_h), ('ind', ind_w, ind_h)]

    for export in export_sizes:

        # Create working image for destructive manipulation
        working_image = pdb.gimp_image_duplicate(image)
        working_layer = pdb.gimp_image_merge_visible_layers(working_image, CLIP_TO_IMAGE)

        size_label = '_' + export[0]
        size_width = float(export[1])
        size_height = float(export[2])

        # Create scale factor to fit working image
        # todo: Use rectangular limits (ie, width != height) as option, rather than square
        # Don't scale twice!
        # if working_image.width > working_image.height:
        #     scale = float(maximum_dimension) / working_image.width
        # else:
        #     scale = float(maximum_dimension) / working_image.height
        # Find scale factor for width and height - lowest will be most significant scaling
        width_scale =  size_width / working_image.width
        height_scale =  size_height / working_image.height

        # Scale and adjust working image
        if width_scale >=1 and height_scale >= 1:
            pass
        elif width_scale <= height_scale:
            pdb.gimp_context_set_interpolation(3)
            pdb.gimp_image_scale(working_image, working_image.width*width_scale, working_image.height*width_scale)
            # Always scale uniformly
            pdb.plug_in_unsharp_mask(working_image, working_layer, 5.0, 0.5, 0)
        elif width_scale > height_scale:
            pdb.gimp_context_set_interpolation(3)
            pdb.gimp_image_scale(working_image, working_image.width*height_scale, working_image.height*height_scale)
            # Always scale uniformly
            pdb.plug_in_unsharp_mask(working_image, working_layer, 5.0, 0.5, 0)

        # Define file & path
        export_file_path = home_dir + '/temp/'
        # todo user-selectable path
        export_file_name = project + '_' + title + size_label + '.png'
        export_file = export_file_path + export_file_name

        # Export working image as PNG
        pdb.file_png_save(working_image, working_layer, export_file, export_file_name, 0, 9, 1, 1, 1, 1, 1)

        # Clean up working image
        pdb.gimp_image_delete(working_image)

    return


register(
    "web_toolbox",                          # proc_name called from command line
    "Creates multiple PNG files for web use",   # info about plug-in
    "Creates multiple PNG files for web use",   # help
    "Paul Vosper",                          # author
    "Paul Vosper",                          # copyright holder for the plug-in
    "2017",                                 # copyright date
    "Web Toolbox",                          # label that the plug-in uses in the menu
    "*",                                    # image types ie: RGB*, GRAY* &etc
    [
        (PF_IMAGE, "image", "Input image", None),
        (PF_DRAWABLE, "drawable", "Input layer", None),
        (PF_STRING, "project", "Project:", "project"),
        (PF_STRING, "title", "Title", "title"),
        (PF_DIRNAME, "dir", "Directory", home_dir),
        (PF_INT, "zoo_w", "Zoom Width", 1024),
        (PF_INT, "zoo_h", "Zoom Height", 768),
        (PF_INT, "dis_w", "Display Width", 512),
        (PF_INT, "dis_h", "Display Height", 384),
        (PF_INT, "ind_w", "Index Width", 256),
        (PF_INT, "ind_h", "Index Height", 192),
    ],                                      # method parameters
    [],                                     # method results
    web_toolbox,                            # name of method that will be called
    menu="<Image>/Local")                   # location in menu bar

main()
