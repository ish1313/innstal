# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-18 14:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HomeBlog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('looking_for_instruction', models.TextField(blank=True, max_length=500, null=True)),
                ('want_to_register_your_warranty_car', models.TextField(blank=True, max_length=500, null=True)),
                ('find_user_manual', models.TextField(blank=True, max_length=500, null=True)),
                ('read_installation_instruction', models.TextField(blank=True, max_length=500, null=True)),
                ('claim_your_warranty_in_future', models.TextField(blank=True, max_length=500, null=True)),
                ('how_it_works', models.TextField(blank=True, max_length=500, null=True)),
            ],
        ),
    ]
