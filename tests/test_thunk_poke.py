# encoding: utf-8
import unittest
import os
import sys
sys.path.append(os.getcwd())
from thunkapi import Thunk

class TestThunkPoke(unittest.TestCase):

    def test_poke_good(self):
        res = Thunk().poke("f6c5970cb00c2c20", "good")
        self.assertEqual("good", res["state"])

    def test_poke_payload(self):
        res = Thunk().poke("f6c5970cb00c2c20", "iffy", "foobar")
        self.assertEqual("foobar", res["payload"])

if __name__ == '__main__':
    unittest.main()
