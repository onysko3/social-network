from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Post


class PostTest(TestCase):

    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(
            username='testuser',
            email='testuser@email.com',
            password='testuser123',
        )

        self.post = Post.objects.create(
            body='Some test text...',
            author=self.user
        )

    def test_post_listing(self):
        self.assertEqual(f'{self.post.body}', 'Some test text...')
        self.assertEqual(self.post.author, self.user)
