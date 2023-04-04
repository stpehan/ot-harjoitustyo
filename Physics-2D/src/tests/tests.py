import unittest
from all.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    def setUp(self):
        self.rectangle = Rectangle(100,100,100)

    def test_stop(self):
        self.rectangle.stop(400)
        self.assertEqual(self.rectangle.velocity, 0)
    
