## Goals for this project

- Export web images within project standards:
    - Source 4000 x 3000
    - Display (<= 1280 x 960)
    - Index (<= 320 x 240)
    - Thumbnail (<= 180 x 240)
    
- Scale pictures using Sinc/Lanczos, then filter using Unsharp Mask

plug-in-unsharp_mask
- run-mode int32
- image image (unused)
- drawable drawable
- radius float (in pixels)
- amount float (strength of effect)
- threshold int32

gimp-context-set-interpolation
- INTERPOLATION-NONE (0)
- INTERPOLATION-LINEAR (1)
- INTERPOLATION-CUBIC (2)
- INTERPOLATION-LANCZOS (3) }

## WTF

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

Method must match register

$todo python version demo

image info
renamer
writing out images


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