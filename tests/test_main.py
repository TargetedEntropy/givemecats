# the inclusion of the tests module is not meant to offer best practices for
# testing in general, but rather to support the `find_packages` example in
# setup.py that excludes installing the "tests" package

import unittest

# from givemecats.main import test_func


class TestSimple(unittest.TestCase):

    def test_zero_is_zero(self):
        self.assertEqual(0, 0)


if __name__ == '__main__':
    unittest.main()
