from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Profile


class ProfileTests(TestCase):

    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(
            username='testuser',
            email='testuser@email.com',
            password='testuser123',
        )
        self.user.profile.first_name = 'John'
        self.user.profile.last_name = 'Doe'
        self.user.profile.slug = 'johndoe'

    def test_profile_listing(self):
        self.assertEqual(f'{self.user.profile.first_name}', 'John')
        self.assertEqual(f'{self.user.profile.last_name}', 'Doe')
        self.assertEqual(f'{self.user.profile.slug}', 'johndoe')

