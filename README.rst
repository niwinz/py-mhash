========
py-mhash
========

Mhash ctypes bindings for Python. It keeps the same interface as hashlib (part of the standard library)

Tested with:

- python 3.3


Current hash algorithms exposed:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- tiger192
- tiger160
- tiger128
- gost


How use it?
^^^^^^^^^^^

.. code-block::

    >>> import mhash
    >>> mhash.Gost(b"hello").hexdigest()
    'a7eb5d08ddf2363f1ea0317a803fcef81d33863c8b2f9f6d7d14951d229f4567'

