import os
import unittest

import mockfs

class ExampleTestCase(unittest.TestCase):
    def setUp(self):
        self.mfs = mockfs.replace_builtins()
        self.mfs.add_entries({'/usr/bin/mockfs-magic': 'magic'})

    def tearDown(self):
        mockfs.restore_builtins()

    def test_using_os_path(self):
        self.assertEqual(os.listdir('/usr/bin'), ['mockfs-magic'])

    def test_using_open(self):
        fh = open('/usr/bin/mockfs-magic')
        data = fh.read()
        fh.close()
        self.assertEqual(data, 'magic')