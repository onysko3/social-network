from django.contrib.auth.models import AbstractUser
from django.dispatch import receiver
from django.db import models
from django.db.models.signals import pre_save, post_save


class CustomUser(AbstractUser):
    pass
