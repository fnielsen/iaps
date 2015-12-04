iaps
====

Utilities for International Affective Picture System (IAPS).

International Affective Picture System 
--------------------------------------
IAPS is a dataset of images scored for affect. It is made by Peter J. Lang, Margaret M. Bradley & Bruce N. Cuthbert. 
The dataset is available for research from the researchers

See also:

* https://en.wikipedia.org/wiki/International_Affective_Picture_System
* http://neuro.compute.dtu.dk/wiki/International_Affective_Picture_System

The Python module
-----------------
This module does not distribute IAPS images. It provides a few utilities useful for researchers
that already have access to the images.

    >>> import iaps
    >>> list_of_10_positive_images = iaps.sample_positive_images(10)
    >>> from PIL import Image
    >>> Image.open(list_of_10_positive_images[3]).show()
