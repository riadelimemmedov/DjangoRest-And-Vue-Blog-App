# Generated by Django 4.0.6 on 2022-07-28 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0001_initial'),
        ('blog', '0010_alter_blog_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='liked',
            field=models.ManyToManyField(blank=True, default=None, related_name='liked', to='user_profile.profile'),
        ),
    ]