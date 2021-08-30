import unittest
from randomimage import get_random_image


class GetRandomImageTestCase(unittest.TestCase):
    def test_get_random_image(self):
        image = get_random_image()

        self.assertTrue(image is not None)


if __name__ == '__main__':
    unittest.main()
