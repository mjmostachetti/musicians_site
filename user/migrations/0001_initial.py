# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('instrument', models.CharField(max_length=30)),
                ('email_address', models.CharField(max_length=70)),
                ('bio', models.TextField()),
                ('website', models.CharField(max_length=100)),
                ('link_to_music', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=30)),
                ('country', models.CharField(max_length=30)),
                ('state', models.CharField(max_length=30)),
                ('member_since', models.DateField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
