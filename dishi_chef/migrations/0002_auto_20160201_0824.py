# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('dishi_chef', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kitchen',
            name='bussiness_types',
        ),
        migrations.RemoveField(
            model_name='member',
            name='date_created',
        ),
        migrations.RemoveField(
            model_name='member',
            name='date_updated',
        ),
        migrations.AddField(
            model_name='kitchen',
            name='bussiness_type',
            field=models.CharField(default=datetime.datetime(2016, 2, 1, 8, 24, 16, 885133, tzinfo=utc), choices=[('type_1', 'Start a Food Business'), ('tpye_2', 'Scale an existing food business'), ('type_3', 'Sell food in my spare time'), ('type_4', 'Offer cooking classes')], max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='kitchen',
            name='kitchen_name',
            field=models.CharField(max_length=50),
        ),
        migrations.RemoveField(
            model_name='kitchen',
            name='kitchen_type',
        ),
        migrations.AddField(
            model_name='kitchen',
            name='kitchen_type',
            field=models.CharField(default=datetime.datetime(2016, 2, 1, 8, 24, 42, 986804, tzinfo=utc), choices=[('type_1', 'bakery'), ('type_2', 'cuisine'), ('type_3', 'African'), ('type_4', 'Other')], max_length=50),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='business_types',
        ),
        migrations.DeleteModel(
            name='kitchen_types',
        ),
    ]
