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
        self.annotations = [
            {
                "id": "1",
                "x": "5",
                "y": "5"
            }
        ]
        self.image = image.Image('testimage.jpg')

    def tearDown(self):
        del self.imageSet
        del self.annotations
        del self.image

    def testImageAddAnnotation(self):
        id, x, y = 1, 5, 5
        self.image.addAnnotation(id, x, y)
        self.assertEqual(self.image.annotations(), self.annotations)


if __name__ == '__main__':
    unittest.main()
