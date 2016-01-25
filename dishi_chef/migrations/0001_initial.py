# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='business_types',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('bussiness_type', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Chef',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('user_name', models.CharField(blank=True, max_length=50)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('profile_picture', models.ImageField(blank=True, upload_to='')),
                ('email_address', models.EmailField(max_length=50)),
                ('date_created', models.DateTimeField(auto_now=True)),
                ('date_updated', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='kitchen_types',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('kitchen_type', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='member',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('user_name', models.CharField(blank=True, max_length=50)),
                ('date_created', models.DateTimeField(auto_now=True)),
                ('date_updated', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
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
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
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
            name='Kitchen',
            fields=[
                ('kitchen_name', models.CharField(blank=True, max_length=50)),
                ('owner', models.OneToOneField(serialize=False, primary_key=True, to='dishi_chef.Chef')),
                ('date_created', models.DateTimeField(auto_now=True)),
                ('date_updated', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='chef',
            name='owner',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('name', models.CharField(blank=True, max_length=50)),
                ('kitchen', models.OneToOneField(serialize=False, primary_key=True, to='dishi_chef.Kitchen')),
                ('date_created', models.DateTimeField(auto_now=True)),
                ('date_updated', models.DateTimeField(auto_now_add=True)),
                ('members', models.ManyToManyField(to='dishi_chef.member')),
            ],
        ),
        migrations.AddField(
            model_name='recipe',
            name='owner',
            field=models.ForeignKey(to='dishi_chef.Kitchen'),
        ),
        migrations.AddField(
            model_name='menu',
            name='owner',
            field=models.ForeignKey(to='dishi_chef.Kitchen'),
        ),
        migrations.AddField(
            model_name='kitchen',
            name='bussiness_types',
            field=models.ManyToManyField(to='dishi_chef.business_types'),
        ),
        migrations.AddField(
            model_name='kitchen',
            name='kitchen_type',
            field=models.ManyToManyField(to='dishi_chef.kitchen_types'),
        ),
    ]
