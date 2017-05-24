# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-24 14:36
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_auto_20170516_1549'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, verbose_name='identifier')),
                ('given_name', models.CharField(max_length=255)),
                ('birthday', models.DateField()),
                ('gender', models.CharField(choices=[('m', 'male'), ('f', 'female'), ('o', 'other'), ('na', 'prefer not to answer')], max_length=2)),
                ('age_at_birth', models.CharField(max_length=25)),
                ('additional_information', models.TextField()),
                ('deleted', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profiles', related_query_name='profiles', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]