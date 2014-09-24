# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='member_since',
        ),
        migrations.AddField(
            model_name='user',
            name='zipcode',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
    ]
