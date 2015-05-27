# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0004_shirt_sid'),
    ]

    operations = [
        migrations.AddField(
            model_name='shirt',
            name='img',
            field=models.ImageField(upload_to='static', default=0),
            preserve_default=False,
        ),
    ]
