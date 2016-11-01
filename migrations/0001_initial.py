# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-11-01 14:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pipeline', '0002_auto_20161024_0848'),
    ]

    operations = [
        migrations.CreateModel(
            name='DemoModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(editable=False, max_length=50, null=True)),
                ('expected_runtime', models.IntegerField(default=0)),
                ('resources_ram_mb', models.IntegerField(default=2000, help_text='Amount of RAM (M) to be allocated for the AviJob')),
                ('resources_cpu_cores', models.IntegerField(default=1, help_text='Number of CPU cores to be allocated to the AviJob')),
                ('inputFile', models.CharField(default='', max_length=1000)),
                ('outputFile', models.CharField(default='', max_length=100)),
                ('request', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='demomodel_model', to='pipeline.AviJobRequest')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
