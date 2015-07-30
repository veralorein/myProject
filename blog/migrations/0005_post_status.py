# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20150728_1956'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='status',
            field=models.CharField(default='0', choices=[('0', 'Dratf'), ('1', 'Published'), ('2', 'Not Published')], max_length=1),
        ),
    ]
