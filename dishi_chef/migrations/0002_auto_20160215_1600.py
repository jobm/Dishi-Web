# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dishi_chef', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Invite',
        ),
        migrations.RemoveField(
            model_name='kitchen',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='menu',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='team',
            name='kitchen',
        ),
        migrations.RemoveField(
            model_name='team',
            name='members',
        ),
        migrations.AddField(
            model_name='chef',
            name='is_chef',
            field=models.BooleanField(default=False),
        ),
        migrations.DeleteModel(
            name='Kitchen',
        ),
        migrations.DeleteModel(
            name='member',
        ),
        migrations.DeleteModel(
            name='Menu',
        ),
        migrations.DeleteModel(
            name='Recipe',
        ),
        migrations.DeleteModel(
            name='Team',
        ),
    ]
