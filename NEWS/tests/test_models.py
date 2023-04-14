import unittest
from django.test import TestCase
from .models import Post


class TestNewsPost(unittest.TestCase):
    pass


class PostModelTest(TestCase):
    
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        django.setup()
    
    def test_post_str(self):
        post = Post(title="Test Post")
        self.assertEqual(str(post), "Test Post")


if __name__ == '__main__':
    unittest.main()