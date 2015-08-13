# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20150810_1156'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='related_slider',
            field=models.ForeignKey(null=True, to='blog.Slider', blank=True),
        ),
    ]
