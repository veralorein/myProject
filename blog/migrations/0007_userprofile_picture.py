# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20150804_1926'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='picture',
            field=models.ImageField(upload_to='profile_images', blank=True),
        ),
    ]
