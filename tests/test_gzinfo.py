import os
import unittest

import gzinfo


class TestGzinfo(unittest.TestCase):
    def test_gzinfo(self):
        filename = os.path.join(os.path.dirname(__file__),
                                'bar.txt.gz')
        info = gzinfo.read_gz_info(filename)

        self.assertIsNotNone(info)
        self.assertEqual('foo.txt', info.fname)


if __name__ == '__main__':
    unittest.main()
