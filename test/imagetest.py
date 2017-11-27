import os
import sys
import inspect
import unittest
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.append(os.path.dirname(currentdir))

import image


class imageTest(unittest.TestCase):

    def setUp(self):

        self.imageSet = {
            "name": "testimage.jpg",
            "points": [
                {
                    "id": "1",
                    "x": "5",
                    "y": "5"
                },
                {
                    "id": "2",
                    "x": "10",
                    "y": "10"
                },
                {
                    "id": "3",
                    "x": "15",
                    "y": "15"
                }
            ]
        }

        self.annotations = (
            [
                {
                    "id": "1",
                    "x": "5",
                    "y": "10"
                }
            ],
            [
                {
                    "id": "1",
                    "x": "10",
                    "y": "15"
                }
            ],
            [
                {
                    "id": "1",
                    "x": "5",
                    "y": "5"
                },
                {
                    "id": "2",
                    "x": "10",
                    "y": "10"
                },
                {
                    "id": "3",
                    "x": "15",
                    "y": "15"
                }
            ]
        )

        self.i = image.Image('testimage.jpg')

    def tearDown(self):
        del self.imageSet
        del self.annotations
        del self.i

    def testImageAddAndUpdateAnnotation(self):
        id = 1
        self.i.addAnnotation(id, 5, 10)
        self.assertEqual(self.i.jsonAnnotations(), self.annotations[0])
        self.i.addAnnotation(id, 10, 15)
        self.assertEqual(self.i.jsonAnnotations(), self.annotations[1])

    def testImageDoesNotAddInvalidIndex(self):
        self.assertEqual(len(self.i), 0)
        self.i.addAnnotation(image.STATUS_PARTIAL, 0, 0)
        self.i.addAnnotation(image.STATUS_EMPTY, 0, 0)
        self.i.addAnnotation(image.STATUS_FULL + 1, 0, 0)
        self.assertEqual(len(self.i), 0)

    def testImageDeleteAnnotation(self):
        self.i.addAnnotation(1, 5, 5)
        self.i.addAnnotation(2, 10, 10)
        self.i.addAnnotation(3, 15, 15)
        self.i.deleteAnnotation(2)
        self.assertEqual(len(self.i), 2)

    def testImageStatus(self):
        self.assertEqual(self.i.status(), image.STATUS_EMPTY)
        self.i.addAnnotation(1, 5, 5)
        self.assertEqual(self.i.status(), image.STATUS_PARTIAL)
        self.i.addAnnotation(2, 10, 10)
        self.assertEqual(self.i.status(), image.STATUS_PARTIAL)
        for id in range(image.STATUS_FULL + 1):
            self.i.addAnnotation(id, 20, 20)
        self.assertEqual(self.i.status(), image.STATUS_FULL)

    def testImageSetJsonAnnotations(self):
        self.i.setJsonAnnotations(self.annotations[2])
        self.assertTrue(self.i.jsonAnnotations() == self.annotations[2])


if __name__ == '__main__':
    unittest.main()
