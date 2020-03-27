import unittest
import time
from decorator import perf


class TestPerf(unittest.TestCase):
    @staticmethod
    @perf
    def fake_func(t, ret=2):
        time.sleep(t)
        return ret

    def test_name(self):
        self.assertEqual(self.fake_func.__name__, 'fake_func')

    def test_return(self):
        self.assertEqual(self.fake_func(1, ret=3), 3)


if __name__ == '__main__':
    unittest.main()
