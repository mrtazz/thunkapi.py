# encoding: utf-8
import unittest
import os
import sys
sys.path.append(os.getcwd())
from thunkapi import Thunk

class TestThunkCheck(unittest.TestCase):

    def setUp(self):
        self.thunk = "822cf0e1def8d629"

    def test_check_state(self):
        res = Thunk().check(self.thunk)
        self.assertEqual("good", res["state"])

    def test_check_name(self):
        res = Thunk().check(self.thunk)
        self.assertEqual("thunkpytest", res["name"])

    def test_check_payload(self):
        res = Thunk().check(self.thunk)
        self.assertEqual("All systems go!", res["payload"])

    def test_check_puuid(self):
        res = Thunk().check(self.thunk)
        self.assertEqual("cef903340c0b4ffa", res["puuid"])

if __name__ == '__main__':
    unittest.main()
