from django.contrib.auth.models import AbstractUser
from django.dispatch import receiver
from django.db import models
from django.db.models.signals import pre_save
from django.urls import reverse


class CustomUser(AbstractUser):
    avatar = models.ImageField('Main photo', upload_to='avatars/', blank=True)
    slug = models.SlugField('Link', unique=True, max_length=150)
    status = models.CharField(max_length=200, blank=True, null=True)
    bio = models.TextField(max_length=1000, blank=True, null=True)
    birthdate = models.DateField('Date of Birth', blank=True, null=True)
    sex = models.CharField(max_length=1, choices=(
        ('M', 'Male'),
        ('F', 'Female'),
    ), blank=True)
    country = models.CharField(max_length=30, blank=True, null=True)
    city = models.CharField(max_length=30, blank=True, null=True)
    education = models.CharField(max_length=100, blank=True, null=True, help_text='')

    def get_absolute_url(self):
        return reverse('profile_detail', kwargs={'slug': self.slug})

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


@receiver(pre_save, sender=CustomUser)
def add_profile_slug(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = instance.username
    if not instance.avatar:
        instance.avatar = 'no_photo.png'