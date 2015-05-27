# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0002_vote_shirt1'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vote',
            old_name='shirt1',
            new_name='shirt',
        ),
    ]
