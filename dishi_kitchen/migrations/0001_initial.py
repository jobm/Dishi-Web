# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('dishi_chef', '0002_auto_20160215_1600'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invite',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('recepient_email', models.EmailField(max_length=254)),
                ('hash_token', models.CharField(unique=True, max_length=36)),
            ],
        ),
        migrations.CreateModel(
            name='Kitchen',
            fields=[
                ('kitchen_name', models.CharField(max_length=50)),
                ('bussiness_type', models.CharField(choices=[('type_1', 'Start a Food Business'), ('tpye_2', 'Scale an existing food business'), ('type_3', 'Sell food in my spare time'), ('type_4', 'Offer cooking classes')], max_length=50)),
                ('kitchen_type', models.CharField(choices=[('type_1', 'bakery'), ('type_2', 'cuisine'), ('type_3', 'African'), ('type_4', 'Other')], max_length=50)),
                ('owner', models.OneToOneField(primary_key=True, to='dishi_chef.Chef', serialize=False)),
                ('date_created', models.DateTimeField(auto_now=True)),
                ('date_updated', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='member',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('user_name', models.CharField(blank=True, max_length=50)),
                ('date_created', models.DateTimeField(auto_now=True)),
                ('date_updated', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('title', models.CharField(max_length=50)),
                ('item_picture', models.ImageField(blank=True, upload_to='')),
                ('description', models.TextField()),
                ('cost', models.FloatField()),
                ('date_created', models.DateTimeField(auto_now=True)),
                ('date_updated', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('title', models.CharField(max_length=50)),
                ('item_picture', models.ImageField(blank=True, upload_to='')),
                ('description', models.TextField()),
                ('likes', models.IntegerField(blank=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(50)])),
                ('date_created', models.DateTimeField(auto_now=True)),
                ('date_updated', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('name', models.CharField(blank=True, max_length=50)),
                ('kitchen', models.OneToOneField(primary_key=True, to='dishi_kitchen.Kitchen', serialize=False)),
                ('date_created', models.DateTimeField(auto_now=True)),
                ('date_updated', models.DateTimeField(auto_now_add=True)),
                ('members', models.ManyToManyField(to='dishi_kitchen.member')),
            ],
        ),
        migrations.AddField(
            model_name='recipe',
            name='owner',
            field=models.ForeignKey(to='dishi_kitchen.Kitchen'),
        ),
        migrations.AddField(
            model_name='menu',
            name='owner',
            field=models.ForeignKey(to='dishi_kitchen.Kitchen'),
        ),
    ]
