import uuid
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse


class Post(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    body = models.TextField(max_length=1000)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='posts')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(get_user_model(), related_name='post_like')

    class Meta:
        ordering = ['-created', '-updated']

    def number_of_likes(self):
        return self.likes.count()

    def get_absolute_url(self):
        return reverse('profile_detail', kwargs={'slug': self.author.slug})

    def __str__(self):
        return self.body[:80]


class PostPicture(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='pictures')
    picture = models.ImageField(upload_to='posts/')
