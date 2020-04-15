# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-03-28 16:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0003_auto_20200328_1631'),
        ('products', '0003_product_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(default='unknown', on_delete=django.db.models.deletion.CASCADE, to='categories.Category'),
        ),
    ]
