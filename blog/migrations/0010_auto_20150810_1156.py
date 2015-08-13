# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import blog.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_page'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slide',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('status', models.IntegerField(choices=[(1, 'Published'), (2, 'Hidden')], default=1)),
                ('title', models.CharField(max_length=32)),
                ('description', models.TextField(null=True, blank=True)),
                ('image', models.ImageField(null=True, upload_to=blog.models.get_blog_file_name, max_length=1024, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('status', models.IntegerField(choices=[(1, 'Published'), (2, 'Hidden')], default=1)),
                ('title', models.CharField(max_length=32)),
                ('description', models.TextField(null=True, blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='slide',
            name='related_slider',
            field=models.ForeignKey(to='blog.Slider'),
        ),
    ]
