## Goals for this project

- Export web images within project standards:
    - Source 4000 x 3000
    - Index (<= 512 x 512)
    - Display (<= 1024 x 1024)
    - Zoom (<= 2048 x 2048)
    
- Scale pictures using Sinc/Lanczos, then filter using Unsharp Mask


## References

- http://gimpbook.com/index.html -- Excellent reference by Akkana Peck
- http://gimpbook.com/scripting/notes.html
- https://www.ibm.com/developerworks/library/os-autogimp/index.html -- Outdated, but good reference
- http://www.pygtk.org
- http://sappersblog.blogspot.com/2017/06/writing-gimp-python-plug-ins.html


## Notes

https://stackoverflow.com/questions/26803732/how-do-i-save-export-all-layers-with-gimps-script-fu

pdb.gimp_file_save(img, background_layer, '/temp/tq84_write_text.png', '?')
by

new_image = pdb.gimp_image_duplicate(img)
layer = pdb.gimp_image_merge_visible_layers(new_image, CLIP_TO_IMAGE)
pdb.gimp_file_save(new_img, layer, '/temp/tq84_write_text.png', '?')
pdb.gimp_image_delete(new_image)
(The last call just "deletes" the new image from program memory, freeing up the resources, of course)


## WTF

Argh: PF_DIRNAME and PF_STRING are returning "wrong" values
>"Specify as many input parameters as there are in the plugin_func and in the same order."

- Python versions
    - GIMP 2.8.22 Python Console
        - Python 2.7.8 (default, Jul 16 2016, 22:25:00)
        - ? So what's the bang node for? Won't load unless #!/usr/bin/env python
    - MacOSX High Sierra
        - Python 2.7.4
    - '\env' should be using Python 3.6
        - python terminal_python_version.py prints 3.6.1

- Reliance on open image file
- Image vs Drawable
- Help not displaying


You can put things in an existing menu:

    menu="<Image>/Edit"
    menu="<Image>/Filters/Blur"
    
Or create your own under an existing tab:

    menu="<Image>/Filters/Custom"

Or even create your own tab:

    menu="<Image>/Custom"

This will create a custom "Python-Fu" menu, not add it to the existing one:

    menu="<Image>/Filters/Python-Fu")


### Error Examples

```Traceback (most recent call last):
  File "/Applications/GIMP.app/Contents/Resources/lib/gimp/2.0/python/gimpfu.py", line 736, in response
    dialog.res = run_script(params)
  File "/Applications/GIMP.app/Contents/Resources/lib/gimp/2.0/python/gimpfu.py", line 361, in run_script
    return apply(function, params)
  File "/Users/paulvosper/Library/Application Support/GIMP/2.8/plug-ins/scale_image.py", line 14, in scale_image
    scale = max/image_width
TypeError: unsupported operand type(s) for /: 'builtin_function_or_method' and 'gimp.PDBFunction'
```



```Traceback (most recent call last):
  File "/Applications/GIMP.app/Contents/Resources/lib/gimp/2.0/python/gimpfu.py", line 736, in response
    dialog.res = run_script(params)
  File "/Applications/GIMP.app/Contents/Resources/lib/gimp/2.0/python/gimpfu.py", line 361, in run_script
    return apply(function, params)
  File "/Users/paulvosper/Library/Application Support/GIMP/2.8/plug-ins/scale_image.py", line 14, in scale_image
    scale = max/image_width
TypeError: unsupported operand type(s) for /: 'int' and 'gimp.PDBFunction'
```


```Traceback (most recent call last):
  File "/Applications/GIMP.app/Contents/Resources/lib/gimp/2.0/python/gimpfu.py", line 736, in response
    dialog.res = run_script(params)
  File "/Applications/GIMP.app/Contents/Resources/lib/gimp/2.0/python/gimpfu.py", line 361, in run_script
    return apply(function, params)
  File "/Users/paulvosper/Library/Application Support/GIMP/2.8/plug-ins/scale_image.py", line 15, in scale_image
    pdb.plug_in_unsharp_mask(1, image, 5.0, 0.5, 0.0)
TypeError: wrong parameter type
```

```Traceback (most recent call last):
  File "/Applications/GIMP.app/Contents/Resources/lib/gimp/2.0/python/gimpfu.py", line 736, in response
    dialog.res = run_script(params)
  File "/Applications/GIMP.app/Contents/Resources/lib/gimp/2.0/python/gimpfu.py", line 361, in run_script
    return apply(function, params)
  File "/Users/paulvosper/Library/Application Support/GIMP/2.8/plug-ins/scale_image.py", line 23, in scale_image
    pdb.gimp_file_save(image, draw, 'test.xcf', '?')
RuntimeError: Could not open 'test.xcf' for writing: Permission denied
```