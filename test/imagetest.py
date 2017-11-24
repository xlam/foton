import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.append(os.path.dirname(currentdir))

import unittest
import image

class ImageTest(unittest.TestCase):

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

        self.image = image.Image('testimage.jpg')

    def tearDown(self):
        del self.imageSet
        del self.annotations
        del self.image

    def testImageAddAndUpdateAnnotation(self):
        id = 1
        self.image.addAnnotation(id, 5, 10)
        self.assertEqual(self.image.annotations(), self.annotations[0])
        self.image.addAnnotation(id, 10, 15)
        self.assertEqual(self.image.annotations(), self.annotations[1])

    def testImageDeleteAnnotation(self):
        self.image.addAnnotation(1, 5, 5)
        self.image.addAnnotation(2, 10, 10)
        self.image.addAnnotation(3, 15, 15)
        self.image.deleteAnnotation(2)
        self.assertEqual(self.image.len(), 2)


if __name__ == '__main__':
    unittest.main()
