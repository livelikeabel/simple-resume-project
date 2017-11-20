# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-11-20 08:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('github_link', models.CharField(max_length=30)),
                ('view_count', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Stack',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('development_language', models.CharField(max_length=30)),
                ('resume', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.Resume')),
            ],
        ),
    ]