"""Interface to IAPS data.

Utility function for reading data and files from the 'International Affective
Picture System' (IAPS).
http://neuro.compute.dtu.dk/wiki/International_Affective_Picture_System

Examples
--------
>>> df = read_scoring()
>>> df.max()
desc      Zipper
IAPS        9941
valmn       8.34
valsd       2.97
aromn       7.35
arosd       2.89
dom1mn      7.71
dom1sd      2.89
dom2mn      6.97
dom2sd      2.69
set           20
dtype: object

>>> from PIL import Image
>>> filenames = sample_positive_images(10)
>>> img = Image.open(filenames[0])
>>> # To show call: img.show()

"""


from __future__ import absolute_import, division, print_function

from os.path import expanduser, join

import pandas as pd


IAPS_DIR = join(expanduser('~'), 'data', 'IAPS 2008 1-20')
IAPS_SCORING_FILENAME = join(IAPS_DIR, 'IAPS Tech Report',
                             'AllSubjects_1-20.txt')


def read_scoring(filename=IAPS_SCORING_FILENAME):
    """Read IAPS scoring.

    Parameters
    ----------
    filename : str
        Filename for the data file with scores.

    Returns
    -------
    df : pandas.DataFrame
        Dataframe with scores.

    Examples
    --------
    >>> df = read_scoring()
    >>> df.ix[df.valmn.argmax(), :].desc
    'Puppies'

    """
    columns = ("desc IAPS valmn valsd aromn arosd dom1mn "
               "dom1sd dom2mn dom2sd set").split()
    df = pd.read_csv(filename, names=columns,
                     sep='\t', skiprows=7, na_values='.')
    df.set = [item[:-1] for item in df.set]     # Remove backslash
    df.set = df.set.astype(int)
    df.IAPS = [str(int(element))
               if int(element) == float(element)
               else "%.1f" % element
               for element in df.IAPS]
    return df


def full_filename(name):
    """Return full filename.

    Parameters
    ----------
    name : str
        Filename without extension corresponding to the elements in the IAPS
        column of the scoring file.

    Returns
    -------
    filename : str
        Filename with path and extension

    """
    full_filename = join(IAPS_DIR, 'IAPS 1-20 Images', name)
    if name in ['6570', '6570.1', '6561', '6560']:
        # A few filenames has the extension '.JPG' instead of '.jpg'!
        full_filename = full_filename + '.JPG'
    else:
        full_filename = full_filename + '.jpg'
    return full_filename


def sample_negative_images(n=None, random_state=None, threshold=3.0):
    """Return sample of negative images.

    Returns
    -------
    filenames : list of str
        List with full filenames.

    Examples
    --------
    >>> filenames = sample_negative_images(10)
    >>> 'jpg' in " ".join(filenames)
    True

    """
    df = read_scoring()
    filenames = df.ix[df.valmn <= threshold, 'IAPS'].sample(
        n=n, random_state=random_state)
    full_filenames = [full_filename(filename) for filename in filenames]
    return full_filenames


def sample_positive_images(n=None, random_state=None, threshold=7.0):
    """Return sample of positive images.

    Returns
    -------
    filenames : list of str
        List with full filenames.

    Examples
    --------
    >>> filenames = sample_positive_images(10)
    >>> 'jpg' in " ".join(filenames)
    True

    """
    df = read_scoring()
    filenames = df.ix[df.valmn >= threshold, 'IAPS'].sample(
        n=n, random_state=random_state)
    full_filenames = [full_filename(filename) for filename in filenames]
    return full_filenames


def sample_neutral_images(n=None, random_state=None, thresholds=(4.0, 6.0)):
    """Return sample of positive images.

    Parameters
    ----------
    n : int
        The number of image filenames to return
    random_state : int
        Seed for the random generator
    thresholds : 2-tuple with float
        Min and max for valence thresholds

    Returns
    -------
    filenames : list of str
        List with full filenames.

    Examples
    --------
    >>> filenames = sample_positive_images(10)
    >>> 'jpg' in " ".join(filenames)
    True

    """
    df = read_scoring()
    filenames = df.ix[(df.valmn >= thresholds[0]) &
                      (df.valmn <= thresholds[1]), 'IAPS'].sample(
                          n=n, random_state=random_state)
    full_filenames = [full_filename(filename) for filename in filenames]
    return full_filenames
