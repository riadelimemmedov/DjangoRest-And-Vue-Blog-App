# Generated by Django 4.0.6 on 2022-07-24 15:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0001_initial'),
        ('blog', '0005_categoryblog_alter_blog_category_delete_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categoryblog',
            options={'verbose_name': 'CategoryBlog', 'verbose_name_plural': 'CategoryBlogs'},
        ),
        migrations.CreateModel(
            name='CommentBlog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog_comments', to='blog.blog')),
                ('profile_comments', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_profile.profile')),
            ],
            options={
                'verbose_name': 'CommentBlog',
                'verbose_name_plural': 'CommentBlogs',
                'ordering': ['-created'],
            },
        ),
    ]
