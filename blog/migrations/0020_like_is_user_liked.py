# Generated by Django 4.0.6 on 2022-08-20 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0019_blog_is_liked'),
    ]

    operations = [
        migrations.AddField(
            model_name='like',
            name='is_user_liked',
            field=models.BooleanField(default=False),
        ),
    ]