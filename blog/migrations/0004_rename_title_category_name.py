# Generated by Django 4.0.6 on 2022-07-24 14:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_remove_category_blogs_remove_category_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='title',
            new_name='name',
        ),
    ]
