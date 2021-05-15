import unittest
import sys
from tmp import pal

class testCaseCube1(unittest.TestCase):
    def test_drome(self):
        self.assertEqual(pal.palan("level"),True)

class testCaseCube2(unittest.TestCase):
    def test_drome(self):
        self.assertEqual(pal.palan("word"),False)

if __name__ == '__main__':
    unittest.main()

