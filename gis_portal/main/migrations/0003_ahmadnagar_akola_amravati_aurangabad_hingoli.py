# Generated by Django 3.1.2 on 2021-03-09 08:04

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20210308_0144'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ahmadnagar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('geom', django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4326)),
                ('field1', models.IntegerField(blank=True, null=True)),
                ('unnamed_0', models.IntegerField(blank=True, db_column='unnamed:_0', null=True)),
                ('school_cod', models.BigIntegerField(blank=True, null=True)),
                ('clrooms', models.IntegerField(blank=True, null=True)),
                ('toiletb', models.IntegerField(blank=True, null=True)),
                ('toilet_g', models.IntegerField(blank=True, null=True)),
                ('mealsinsch', models.IntegerField(blank=True, null=True)),
                ('electric_y', models.IntegerField(blank=True, null=True)),
                ('library_yn', models.IntegerField(blank=True, null=True)),
                ('pground_yn', models.IntegerField(blank=True, null=True)),
                ('bookinlib', models.IntegerField(blank=True, null=True)),
                ('water', models.IntegerField(blank=True, null=True)),
                ('medchk_yn', models.IntegerField(blank=True, null=True)),
                ('ramps_yn', models.IntegerField(blank=True, null=True)),
                ('computer', models.IntegerField(blank=True, null=True)),
                ('distname', models.CharField(blank=True, max_length=10, null=True)),
                ('school_nam', models.CharField(blank=True, max_length=100, null=True)),
                ('block_name', models.CharField(blank=True, max_length=13, null=True)),
                ('cluster_na', models.CharField(blank=True, max_length=22, null=True)),
                ('village_na', models.CharField(blank=True, max_length=21, null=True)),
                ('pincode', models.IntegerField(blank=True, null=True)),
                ('unnamed_7', models.CharField(blank=True, db_column='unnamed:_7', max_length=1, null=True)),
                ('district', models.CharField(blank=True, max_length=10, null=True)),
            ],
            options={
                'db_table': 'ahmadnagar',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Akola',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('geom', django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4326)),
                ('field1', models.IntegerField(blank=True, null=True)),
                ('unnamed_0', models.IntegerField(blank=True, db_column='unnamed:_0', null=True)),
                ('school_cod', models.BigIntegerField(blank=True, null=True)),
                ('clrooms', models.IntegerField(blank=True, null=True)),
                ('toiletb', models.IntegerField(blank=True, null=True)),
                ('toilet_g', models.IntegerField(blank=True, null=True)),
                ('mealsinsch', models.IntegerField(blank=True, null=True)),
                ('electric_y', models.IntegerField(blank=True, null=True)),
                ('library_yn', models.IntegerField(blank=True, null=True)),
                ('pground_yn', models.IntegerField(blank=True, null=True)),
                ('bookinlib', models.IntegerField(blank=True, null=True)),
                ('water', models.IntegerField(blank=True, null=True)),
                ('medchk_yn', models.IntegerField(blank=True, null=True)),
                ('ramps_yn', models.IntegerField(blank=True, null=True)),
                ('computer', models.IntegerField(blank=True, null=True)),
                ('distname', models.CharField(blank=True, max_length=5, null=True)),
                ('school_nam', models.CharField(blank=True, max_length=100, null=True)),
                ('block_name', models.CharField(blank=True, max_length=11, null=True)),
                ('cluster_na', models.CharField(blank=True, max_length=25, null=True)),
                ('village_na', models.CharField(blank=True, max_length=24, null=True)),
                ('pincode', models.IntegerField(blank=True, null=True)),
                ('unnamed_7', models.CharField(blank=True, db_column='unnamed:_7', max_length=1, null=True)),
                ('district', models.CharField(blank=True, max_length=5, null=True)),
            ],
            options={
                'db_table': 'akola',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Amravati',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('geom', django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4326)),
                ('field1', models.IntegerField(blank=True, null=True)),
                ('unnamed_0', models.IntegerField(blank=True, db_column='unnamed:_0', null=True)),
                ('school_cod', models.BigIntegerField(blank=True, null=True)),
                ('clrooms', models.IntegerField(blank=True, null=True)),
                ('toiletb', models.IntegerField(blank=True, null=True)),
                ('toilet_g', models.IntegerField(blank=True, null=True)),
                ('mealsinsch', models.IntegerField(blank=True, null=True)),
                ('electric_y', models.IntegerField(blank=True, null=True)),
                ('library_yn', models.IntegerField(blank=True, null=True)),
                ('pground_yn', models.IntegerField(blank=True, null=True)),
                ('bookinlib', models.IntegerField(blank=True, null=True)),
                ('water', models.IntegerField(blank=True, null=True)),
                ('medchk_yn', models.IntegerField(blank=True, null=True)),
                ('ramps_yn', models.IntegerField(blank=True, null=True)),
                ('computer', models.IntegerField(blank=True, null=True)),
                ('distname', models.CharField(blank=True, max_length=8, null=True)),
                ('school_nam', models.CharField(blank=True, max_length=72, null=True)),
                ('block_name', models.CharField(blank=True, max_length=15, null=True)),
                ('cluster_na', models.CharField(blank=True, max_length=23, null=True)),
                ('village_na', models.CharField(blank=True, max_length=22, null=True)),
                ('pincode', models.CharField(blank=True, max_length=15, null=True)),
                ('unnamed_7', models.IntegerField(blank=True, db_column='unnamed:_7', null=True)),
                ('district', models.CharField(blank=True, max_length=8, null=True)),
            ],
            options={
                'db_table': 'amravati',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Aurangabad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('geom', django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4326)),
                ('field1', models.IntegerField(blank=True, null=True)),
                ('unnamed_0', models.IntegerField(blank=True, db_column='unnamed:_0', null=True)),
                ('school_cod', models.BigIntegerField(blank=True, null=True)),
                ('clrooms', models.IntegerField(blank=True, null=True)),
                ('toiletb', models.IntegerField(blank=True, null=True)),
                ('toilet_g', models.IntegerField(blank=True, null=True)),
                ('mealsinsch', models.IntegerField(blank=True, null=True)),
                ('electric_y', models.IntegerField(blank=True, null=True)),
                ('library_yn', models.IntegerField(blank=True, null=True)),
                ('pground_yn', models.IntegerField(blank=True, null=True)),
                ('bookinlib', models.IntegerField(blank=True, null=True)),
                ('water', models.IntegerField(blank=True, null=True)),
                ('medchk_yn', models.IntegerField(blank=True, null=True)),
                ('ramps_yn', models.IntegerField(blank=True, null=True)),
                ('computer', models.IntegerField(blank=True, null=True)),
                ('distname', models.CharField(blank=True, max_length=24, null=True)),
                ('school_nam', models.CharField(blank=True, max_length=87, null=True)),
                ('block_name', models.CharField(blank=True, max_length=10, null=True)),
                ('cluster_na', models.CharField(blank=True, max_length=26, null=True)),
                ('village_na', models.CharField(blank=True, max_length=24, null=True)),
                ('pincode', models.IntegerField(blank=True, null=True)),
                ('unnamed_7', models.CharField(blank=True, db_column='unnamed:_7', max_length=1, null=True)),
                ('district', models.CharField(blank=True, max_length=10, null=True)),
            ],
            options={
                'db_table': 'aurangabad',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Hingoli',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('geom', django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4326)),
                ('field1', models.IntegerField(blank=True, null=True)),
                ('unnamed_0', models.IntegerField(blank=True, db_column='unnamed:_0', null=True)),
                ('school_cod', models.BigIntegerField(blank=True, null=True)),
                ('clrooms', models.IntegerField(blank=True, null=True)),
                ('toiletb', models.IntegerField(blank=True, null=True)),
                ('toilet_g', models.IntegerField(blank=True, null=True)),
                ('mealsinsch', models.IntegerField(blank=True, null=True)),
                ('electric_y', models.IntegerField(blank=True, null=True)),
                ('library_yn', models.IntegerField(blank=True, null=True)),
                ('pground_yn', models.IntegerField(blank=True, null=True)),
                ('bookinlib', models.IntegerField(blank=True, null=True)),
                ('water', models.IntegerField(blank=True, null=True)),
                ('medchk_yn', models.IntegerField(blank=True, null=True)),
                ('ramps_yn', models.IntegerField(blank=True, null=True)),
                ('computer', models.IntegerField(blank=True, null=True)),
                ('distname', models.CharField(blank=True, max_length=7, null=True)),
                ('school_nam', models.CharField(blank=True, max_length=83, null=True)),
                ('block_name', models.CharField(blank=True, max_length=14, null=True)),
                ('cluster_na', models.CharField(blank=True, max_length=20, null=True)),
                ('village_na', models.CharField(blank=True, max_length=27, null=True)),
                ('pincode', models.IntegerField(blank=True, null=True)),
                ('unnamed_7', models.CharField(blank=True, db_column='unnamed:_7', max_length=1, null=True)),
                ('district', models.CharField(blank=True, max_length=7, null=True)),
            ],
            options={
                'db_table': 'hingoli',
                'managed': False,
            },
        ),
    ]
