# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import blog.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('status', models.IntegerField(choices=[(1, 'Published'), (2, 'Hidden')], default=1)),
                ('title', models.CharField(max_length=32)),
                ('slug', models.SlugField(unique=True)),
                ('content', models.TextField()),
                ('featured_image', models.ImageField(blank=True, null=True, upload_to=blog.models.get_blog_file_name, max_length=1024)),
            ],
        ),
    ]
