# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vote',
            name='shirt1',
            field=models.ForeignKey(to='poll.Shirt', default=0),
            preserve_default=False,
        ),
    ]
