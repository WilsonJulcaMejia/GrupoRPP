# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-21 02:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20170520_2054'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'Redactore', 'verbose_name_plural': 'Redactores'},
        ),
    ]