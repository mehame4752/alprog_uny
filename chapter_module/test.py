import unittest

from arithmetic import add

class TestAdd(unittest.TestCase):
    def test_int(self):
        """
            test for integer argument
        """
        result = add(4, 5)
        self.assertEqual(result, 9)

if __name__ == '__main__':
    unittest.main()