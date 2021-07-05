from django.contrib.auth import get_user_model
from django.dispatch import receiver
from django.urls import reverse
from django.db import models
from django.db.models.signals import pre_save, post_save


class Profile(models.Model):
    first_name = models.CharField('Name', max_length=50, null=True)
    last_name = models.CharField('Surname', max_length=50, null=True)
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
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, related_name='profile')

    def get_absolute_url(self):
        return reverse('profile_detail', kwargs={'slug': self.slug})

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


@receiver(pre_save, sender=Profile)
def add_profile_slug(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = instance.user.username
    if not instance.avatar:
        instance.avatar = 'no_photo.png'


@receiver(post_save, sender=get_user_model())
def user_create_create_profile(sender, instance, created, *args, **kwargs):
    if created:
        Profile.objects.create(user=instance)
