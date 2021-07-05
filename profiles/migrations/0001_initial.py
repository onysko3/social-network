# Generated by Django 3.2.5 on 2021-07-05 14:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, null=True, verbose_name='Name')),
                ('last_name', models.CharField(max_length=50, null=True, verbose_name='Surname')),
                ('avatar', models.ImageField(blank=True, upload_to='avatars/', verbose_name='Main photo')),
                ('slug', models.SlugField(max_length=150, unique=True, verbose_name='Link')),
                ('status', models.CharField(blank=True, max_length=200, null=True)),
                ('bio', models.TextField(blank=True, max_length=1000, null=True)),
                ('birthdate', models.DateField(blank=True, null=True, verbose_name='Date of Birth')),
                ('sex', models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('country', models.CharField(blank=True, max_length=30, null=True)),
                ('city', models.CharField(blank=True, max_length=30, null=True)),
                ('education', models.CharField(blank=True, max_length=100, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]