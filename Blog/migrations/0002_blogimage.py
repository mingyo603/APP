# Generated by Django 5.2.1 on 2025-05-25 18:01

import Blog.models
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogImage',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('image', models.ImageField(upload_to=Blog.models.blog_image_upload_path)),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='Blog.blog')),
            ],
        ),
    ]
