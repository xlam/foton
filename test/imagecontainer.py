import os
import sys
import inspect
import unittest
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.append(os.path.dirname(currentdir))

import image


class imageContainerTest(unittest.TestCase):

    def setUp(self):
        self.ic = image.ImageContainer()

    def tearDown(self):
        del self.ic

    def testImageContainerAdd(self):
        self.assertEqual(len(self.ic), 0)
        self.ic.add(image.Image('image.jpg'))
        self.assertEqual(len(self.ic), 1)

    def testImageContainerRemove(self):
        i1 = image.Image('image.jpg')
        i2 = image.Image('image.jpg')
        self.ic.add(i1)
        self.ic.add(i2)
        self.assertEqual(len(self.ic), 2)
        self.ic.remove(i2)
        self.assertEqual(len(self.ic), 1)

    @unittest.skip('Not implemented')
    def testImageContainerLoad(self):
        self.ic.load('img')
        self.assertEqual(len(self.ic), 5)


if __name__ == '__main__':
    unittest.main()
