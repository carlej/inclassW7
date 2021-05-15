import unittest
import sys
from tmp import wordc

class testCaseCube1(unittest.TestCase):
    def test_good(self):
        self.assertEqual(wordc.wordcount("this is a test"),4)
    def test_bad(self):
        self.assertEqual(wordc.wordcount("this is a bad test"),4)
        

if __name__ == '__main__':
    unittest.main()
