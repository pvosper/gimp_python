##WTF

- Python versions
    - GIMP 2.8.22 Python Console
Python 2.7.8 (default, Jul 16 2016, 22:25:00)
    - MacOSX High Sierra 2.7.4
- Menu locations
- Reliance on open image file

Method moust match register


You can put things in an existing menu:

    menu="<Image>/Edit"
    menu="<Image>/Filters/Blur"
    
Or create your own under an existing tab:

    menu="<Image>/Filters/Custom"

Or even create your own tab:

    menu="<Image>/Custom"

This will create a custom "Python-Fu" menu, not add it to the existing one:

    menu="<Image>/Filters/Python-Fu")