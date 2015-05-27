# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0003_auto_20150525_1456'),
    ]

    operations = [
        migrations.AddField(
            model_name='shirt',
            name='sid',
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
    ]
