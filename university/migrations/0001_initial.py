# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('regnum', models.CharField(max_length=100)),
                ('semester', models.CharField(max_length=10, choices=[(b'1', b'One'), (b'2', b'Two')])),
                ('year', models.CharField(max_length=10, choices=[(b'2014', b'2014'), (b'2013', b'2013')])),
                ('subject', models.CharField(max_length=20, choices=[(b'Python', b'Python'), (b'Java', b'Java')])),
                ('mark', models.CharField(max_length=100)),
                ('result', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('firstname', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('registernum', models.CharField(unique=True, max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('department', models.CharField(max_length=10, choices=[(b'IT', b'IT'), (b'CS', b'CS')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
