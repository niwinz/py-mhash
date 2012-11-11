# -*- coding: utf-8 -*-

from . import api
import binascii

class BaseHash(object):
    _hash_type = None
    _result = None

    def __init__(self, data=None):
        self.td = api.lib.mhash_init(self._hash_type)
        if self.td is None:
            raise RuntimeError("Unexpected error")

        if data is not None:
            if not isinstance(data, bytes):
                raise RuntimeError("data must be bytes instance")

            api.lib.mhash(self.td, data, len(data))

    def update(self, data):
        if self._result is not None:
            return

        if not isinstance(data, bytes):
            raise RuntimeError("data must be bytes instance")

        api.lib.mhash(self.td, data, len(data))

    def digest(self):
        if self._result is not None:
            return self._result

        size = api.lib.mhash_get_block_size(self._hash_type)
        self._result = api.lib.mhash_end(self.td)
        if len(self._result) > size:
            self._result = self._result[:size]

        return self._result

    def hexdigest(self):
        return binascii.hexlify(self.digest())
