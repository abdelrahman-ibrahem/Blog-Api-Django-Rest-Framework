# blog/tests.py
from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Post

class TestPost(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="abdo",
            email="abdo@gmail.com",
            password="password"
        )
    
    def test_post_model(self):
        post = Post.objects.create(auther=self.user , title='first' ,body='first')
        self.assertEqual(post.auther , self.user)
        self.assertEqual(post.title , 'first')
        self.assertEqual(post.body , 'first')
