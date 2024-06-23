import unittest
import tst

class TestMain(unittest.TestCase):
    def tst_do_stuff(self):
        test_param = 10
        result = tst.do_stuff(test_param)
        self.assertEqual(result,15)

unittest.tst()