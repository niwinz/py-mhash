# -*- coding: utf-8 -*-

from . import api
from . import base


class Tiger(base.BaseHash):
    _hash_type = api.MHASH_TIGER192


class Tiger128(base.BaseHash):
    _hash_type = api.MHASH_TIGER128


class Tiger160(base.BaseHash):
    _hash_type = api.MHASH_TIGER160


Tiger192 = Tiger
