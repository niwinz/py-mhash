# -*- coding: utf-8 -*-

from . import api
from . import base


class Gost(base.BaseHash):
    _hash_type = api.MHASH_GOST
