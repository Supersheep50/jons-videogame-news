import unittest
from django.test import TestCase
from NEWS.models import Post


class TestNewsPost(unittest.TestCase):
    pass


unittest.main()


class PostModelTest(TestCase):
    
    def test_post_str(self):
        post = Post(title="Test Post")
        self.assertEqual(str(post), "Test Post")


unittest.main()
