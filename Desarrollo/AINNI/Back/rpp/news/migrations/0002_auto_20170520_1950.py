# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-21 00:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='new',
            options={'verbose_name': 'Noticia', 'verbose_name_plural': 'Noticias'},
        ),
    ]