import os
import sys
import inspect
import unittest
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.append(os.path.dirname(currentdir))

import image


class ImageContainerTest(unittest.TestCase):

    def setUp(self):
        self.ic = image.ImageContainer()
        self.files = os.path.abspath(os.getcwd() + os.sep + 'files')

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

    def testPicklePersistance(self):
        self.ic.add(image.Image('image1.jpg'))
        self.ic.add(image.Image('image2.jpg'))
        filename = self.files + os.sep + 'save.ftn'
        self.ic.saveToPickle(filename)
        ic2 = image.ImageContainer()
        ic2.loadFromPickle(filename)
        self.assertTrue(len(self.ic) == len(ic2))
        for image1, image2 in zip(self.ic, ic2):
            self.assertTrue(image1.name == image2.name)
        os.unlink(filename)


if __name__ == '__main__':
    unittest.main()
