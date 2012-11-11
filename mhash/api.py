# -*- coding: utf-8 -*-

import ctypes
import ctypes.util

def load_library():
    libpath = ctypes.util.find_library('mhash')
    return ctypes.CDLL(libpath)


MHASH_TIGER192 = 7
MHASH_TIGER128 = 14
MHASH_TIGER160 = 15
MHASH_GOST = 8
MHASH_WHIRLPOOL = 22


try:
    lib = load_library()
    lib.mhash_init.argtypes = [ctypes.c_int]
    lib.mhash_init.restype = ctypes.c_void_p

    lib.mhash.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_int]
    lib.mhash_end.argtypes = [ctypes.c_void_p]
    lib.mhash_end.restype = ctypes.c_char_p

    lib.mhash_get_block_size.argtypes = [ctypes.c_int]
    lib.mhash_get_block_size.restype = ctypes.c_int
except AttributeError:
    raise ImportError('mhash shared library not found or incompatible')
except (OSError, IOError):
    raise ImportError('mhash shared library not found.\n'
                      'you probably had not installed mhash library.\n')
