# Generated by Django 4.0.6 on 2022-08-14 16:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_alter_like_profile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='like',
            old_name='profile',
            new_name='user',
        ),
    ]
