# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-29 23:24
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('image', models.ImageField(blank=True, upload_to='ads/photo', verbose_name='Photo')),
                ('description', models.TextField(blank=True, verbose_name='Description')),
            ],
        ),
        migrations.CreateModel(
            name='UserAd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ad_type', models.IntegerField(choices=[(0, 'Auto save'), (1, 'Manual save')], verbose_name='Ad Type')),
                ('added_at', models.DateTimeField(auto_now_add=True, verbose_name='Added at')),
                ('ad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Ad')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
