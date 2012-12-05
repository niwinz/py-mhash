
import unittest
import mhashlib

class MHashlibTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.sample_data = b"hello\n\n"

    @classmethod
    def tearDownClass(cls):
        pass

    def test_gost_hash(self):
        hash = mhashlib.gost(self.sample_data)
        valid_digest = b'a2c0810ccbb997eb2e029e7e4186535ef4efae43fdcb49afb4933303f649f8db'
        self.assertEqual(valid_digest, hash.hexdigest())

    def test_tiger192_hash(self):
        hash = mhashlib.tiger192(self.sample_data)
        valid_digest = b'3655e96f537401e1c5ac4197ac22594e6d0a740c664e7263'
        self.assertEqual(valid_digest, hash.hexdigest())
