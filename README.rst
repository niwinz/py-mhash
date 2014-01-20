========
py-mhash
========

Modern mhash bindings for Python (build with ctypes). It keeps the same interface as hashlib (part of the standard library)

**Tested with**: python >= 3.2, python >= 2.7, pypy >= 1.9

Actually supports all hash algorithms as mhash library: crc, md5, sha*, ripemd*, tiger*, haval*, gost, adler, whirlpool, snefru*

How install it?
^^^^^^^^^^^^^^^

You can install this module from python package index: `pip install  py-mhash`


How use it?
^^^^^^^^^^^

Example of use gost hash algorithm:

.. code-block:: python

    >>> import mhashlib
    >>> mhashlib.gost(b"hello").hexdigest()
    'a7eb5d08ddf2363f1ea0317a803fcef81d33863c8b2f9f6d7d14951d229f4567'


Run tests
^^^^^^^^^

.. code-block:: console

    python -m unittest -vv


.. image:: https://d2weczhvl823v0.cloudfront.net/niwibe/py-mhash/trend.png
   :alt: Bitdeli badge
   :target: https://bitdeli.com/free

