import unittest
import imagetest
import imagecontainer

if __name__ == '__main__':
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    suite.addTests(loader.loadTestsFromTestCase(imagetest.ImageTest))
    suite.addTests(
        loader.loadTestsFromTestCase(imagecontainer.ImageContainerTest))
    runner = unittest.TextTestRunner()
    runner.run(suite)
